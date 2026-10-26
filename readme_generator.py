from datetime import datetime
from pathlib import Path
import math
import re
import unicodedata
from zoneinfo import ZoneInfo

import pandas as pd

from destinations import normalize_destination
from hall_crowd import hourly_forecast

CHART_DAYS = 90
PLACEHOLDER_RE = re.compile(r'\{([a-z_]+)\}')


def get_data_path():
    data_path = Path('./data/logs')
    csv_list = list(data_path.glob('*.csv'))
    return csv_list

def merge_csv_files(csv_files):
    dataframes = [pd.read_csv(file) for file in csv_files]
    merged_df = pd.concat(dataframes, ignore_index=True)
    merged_df['flight_title'] = merged_df['flight_title'].fillna('N/A').map(normalize_destination)
    merged_df.to_csv('./data/all_departures_all_dates.csv', index=False)
    return merged_df

def rows_for_charts(merged_df):
    chart_df = merged_df.copy()
    if 'board' in chart_df.columns:
        board = chart_df['board'].fillna('today')
        chart_df = chart_df[board != 'tomorrow']
    return chart_df

def daily_counts(chart_df):
    result = chart_df.groupby(chart_df['date']).agg(
        count = ('date','size'),
        unique_destinations = ('flight_title','nunique')
    ).reset_index()
    return result.sort_values('date')

def quarter_key(date):
    year, month, _day = str(date).split('-')
    quarter = (int(month) - 1) // 3 + 1
    return f'{year} Q{quarter}'

def quarter_averages(daily_df):
    frame = daily_df.copy()
    frame['quarter'] = frame['date'].map(quarter_key)
    grouped = frame.groupby('quarter', sort=False).agg(
        avg_departures=('count', 'mean'),
        avg_destinations=('unique_destinations', 'mean'),
    ).reset_index()
    grouped['_sort'] = grouped['quarter'].map(lambda label: (int(label[:4]), int(label[-1])))
    return grouped.sort_values('_sort').drop(columns='_sort')

def sankey_label(name):
    text = str(name)
    for source, target in (
        ('ł', 'l'), ('Ł', 'L'), ('ø', 'o'), ('Ø', 'O'),
        ('đ', 'd'), ('Đ', 'D'), ('æ', 'ae'), ('Æ', 'AE'),
        ('œ', 'oe'), ('ß', 'ss'),
    ):
        text = text.replace(source, target)
    text = unicodedata.normalize('NFKD', text)
    text = ''.join(char for char in text if not unicodedata.combining(char))
    text = text.encode('ascii', 'ignore').decode('ascii')
    text = text.replace(',', ' / ').replace('"', '').replace('/', ' ')
    text = re.sub(r'\s+', ' ', text).strip()
    return text or 'Unknown'

def sparse_date_labels(dates, every=7):
    labels = []
    for index, date in enumerate(dates):
        if index % every == 0 or index == len(dates) - 1:
            _year, month, day = str(date).split('-')
            labels.append(f'{day}.{month}')
        else:
            labels.append(' ')
    return ', '.join(f'"{label}"' for label in labels)

def forecast_date(dates, today):
    ordered = sorted({str(date) for date in dates})
    if not ordered:
        return None
    upcoming = [date for date in ordered if date > today.isoformat()]
    if upcoming:
        return upcoming[0]
    if today.isoformat() in ordered:
        return today.isoformat()
    return ordered[-1]

def terminal_forecast(merged_df, today):
    chosen = forecast_date(merged_df['date'], today)
    if chosen is None:
        return 'No scheduled flights yet.'
    rows = merged_df[merged_df['date'].astype(str) == chosen].to_dict('records')
    hours = hourly_forecast(rows)
    if not hours:
        return f'**{chosen}**\n\nNo scheduled times for this day.'
    lines = [f'**{chosen}**', '', '| Hour | Terminal | Why |', '| --- | --- | --- |']
    for hour, _plane_loads, word, reason in hours:
        lines.append(f'| {hour} | {word} | {reason} |')
    return '\n'.join(lines)

def chart_city(name):
    label = sankey_label(name).split(' / ')[0]
    label = re.sub(r'\s*\([^)]*\)', '', label).strip()
    return label or 'Unknown'

def destination_counts(chart_df):
    cities = chart_df['flight_title'].map(chart_city)
    counts = cities.value_counts()
    counts = counts.drop(labels=['Tallinn', 'Unknown'], errors='ignore')
    return counts

def scrape_span(chart_df):
    parsed = pd.to_datetime(chart_df['date'])
    start = parsed.min()
    end = parsed.max()
    years = max((end - start).days, 1) / 365.25
    return start.date(), years

def since_label(start):
    months = ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec')
    return f'{start.day} {months[start.month - 1]} {start.year}'

def destination_chart(counts, years, width=32):
    if counts.empty:
        return 'No destinations yet.'
    peak = int(counts.iloc[0]) or 1
    name_width = max(len(str(name)) for name in counts.index)
    lines = ['```']
    for name, count in counts.items():
        per_year = int(count) / years
        bar = '█' * max(1, round(width * int(count) / peak))
        lines.append(f'{name:<{name_width}}  {int(count):>5}  {per_year:>6.1f}/yr  {bar}')
    lines.append('```')
    return '\n'.join(lines)

def get_chart_values(merged_df):
    chart_df = rows_for_charts(merged_df)
    result_1 = daily_counts(chart_df).tail(CHART_DAYS)
    counts = destination_counts(chart_df)
    result_2 = counts.rename_axis('flight_title').reset_index(name='count')
    return result_1, result_2

def render_template(template, data):
    def replace(match):
        key = match.group(1)
        if key not in data:
            return match.group(0)
        return str(data[key])

    return PLACEHOLDER_RE.sub(replace, template)

def generate_readme(template_path, data, output_path):
    template = Path(template_path).read_text()
    readme_content = render_template(template, data)
    Path(output_path).write_text(readme_content)

def create_chart_dates(dataframe, column):
    return sparse_date_labels(list(dataframe[column]))


def number_list(values, digits=None):
    rendered = []
    for value in values:
        if digits is None:
            rendered.append(str(value))
        else:
            rendered.append(f'{float(value):.{digits}f}')
    return '[' + ', '.join(rendered) + ']'

def chart_limit(values):
    peak = max(values) if len(values) else 0
    return int(math.ceil(peak + max(peak / 10, 1)))

def main():
    merged = merge_csv_files(get_data_path())
    chart_df = rows_for_charts(merged)
    daily = daily_counts(chart_df)
    recent = daily.tail(CHART_DAYS)
    quarters = quarter_averages(daily)
    _chart_values_df, destination_df = get_chart_values(merged)
    started, years = scrape_span(chart_df)
    today = datetime.now(ZoneInfo('Europe/Tallinn')).date()

    chart_data = {
        'title': 'Departures by day',
        'x_axis': create_chart_dates(recent, 'date'),
        'y_axis': '# departures',
        'bar_values': recent['count'].to_list(),
        'ymax': chart_limit(recent['count'].to_list()),
        'quarter_x': ', '.join(f'"{quarter}"' for quarter in quarters['quarter']),
        'quarter_bar': number_list(quarters['avg_departures'], 1),
        'quarter_line': number_list(quarters['avg_destinations'], 1),
        'quarter_ymax': chart_limit(quarters['avg_departures'].to_list()),
        'terminal_forecast': terminal_forecast(merged, today),
        'since_date': since_label(started),
        'destination_chart': destination_chart(
            destination_df.set_index('flight_title')['count'],
            years,
        ),
    }

    generate_readme('readme_template.yml', chart_data, 'README.md')

if __name__ == "__main__":
    main()
