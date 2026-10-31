from datetime import datetime, timedelta
from pathlib import Path
import math
import re
import unicodedata
from zoneinfo import ZoneInfo

import pandas as pd

from destinations import normalize_destination
from hall_crowd import hourly_flight_counts

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

TERMINAL_HOURS = [f'{hour:02d}:00' for hour in range(4, 23)]
WEEKDAYS = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')
MONTHS = ('January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December')


def short_date(day):
    return f'{day.day} {MONTHS[day.month - 1][:3]}'

def rows_on(merged_df, day):
    if merged_df.empty or 'date' not in merged_df.columns:
        return []
    key = day.isoformat()
    matched = merged_df[merged_df['date'].astype(str).str.slice(0, 10) == key]
    return matched.to_dict('records')

def counts_for(rows):
    hours = hourly_flight_counts(rows)
    if not hours:
        return None
    return dict(hours)

def flight_cell(counts, hour):
    if counts is None:
        return '—'
    return str(counts.get(hour, 0))

def terminal_forecast(merged_df, today):
    tomorrow = today + timedelta(days=1)
    today_counts = counts_for(rows_on(merged_df, today))
    tomorrow_counts = counts_for(rows_on(merged_df, tomorrow))
    today_label = short_date(today)
    tomorrow_label = short_date(tomorrow)
    lines = [
        f'| Hour | {today_label} | Flights | | {tomorrow_label} | Flights |',
        '| --- | --- | ---: | --- | --- | ---: |',
    ]
    for hour in TERMINAL_HOURS:
        lines.append(
            f'| {hour} | {today_label} | {flight_cell(today_counts, hour)}'
            f' | | {tomorrow_label} | {flight_cell(tomorrow_counts, hour)} |'
        )
    return '\n'.join(lines)

def _average(values):
    return sum(values) / len(values)

def _named_extreme(pairs):
    busiest_at = max(range(len(pairs)), key=lambda index: (pairs[index][1], -index))
    quietest_at = min(range(len(pairs)), key=lambda index: (pairs[index][1], index))
    return pairs[busiest_at], pairs[quietest_at]

def _one_decimal(value):
    return f'{value:.1f}'

def terminal_history(merged_df, today):
    if merged_df.empty or 'date' not in merged_df.columns:
        return 'No history yet.'
    frame = merged_df.copy()
    frame['day'] = frame['date'].astype(str).str.slice(0, 10)
    frame = frame[frame['day'] <= today.isoformat()]
    by_day = {}
    for day, group in frame.groupby('day'):
        counts = counts_for(group.to_dict('records'))
        if counts is None:
            continue
        by_day[day] = counts
    if not by_day:
        return 'No history yet.'

    hour_pairs = [
        (hour, _average([counts[hour] for counts in by_day.values()]))
        for hour in TERMINAL_HOURS
    ]
    weekday_peaks = {name: [] for name in WEEKDAYS}
    month_peaks = {name: [] for name in MONTHS}
    for day, counts in by_day.items():
        parsed = datetime.strptime(day, '%Y-%m-%d')
        peak = max(counts.values())
        weekday_peaks[WEEKDAYS[parsed.weekday()]].append(peak)
        month_peaks[MONTHS[parsed.month - 1]].append(peak)
    weekday_pairs = [
        (name, _average(peaks))
        for name, peaks in weekday_peaks.items()
        if peaks
    ]
    month_pairs = [
        (name, _average(peaks))
        for name, peaks in month_peaks.items()
        if peaks
    ]
    busiest_hour, quietest_hour = _named_extreme(hour_pairs)
    busiest_weekday, quietest_weekday = _named_extreme(weekday_pairs)
    busiest_month, quietest_month = _named_extreme(month_pairs)
    first = min(by_day)
    last = max(by_day)
    lines = [
        (
            f'Averages from {since_label(datetime.strptime(first, "%Y-%m-%d").date())}'
            f' through {since_label(datetime.strptime(last, "%Y-%m-%d").date())},'
            f' {len(by_day)} days.'
            ' Weekday and month numbers are the average of that day’s busiest hour.'
        ),
        '',
        (
            f'{busiest_hour[0]} is the busiest hour ({_one_decimal(busiest_hour[1])} flights).'
            f' {quietest_hour[0]} is the quietest ({_one_decimal(quietest_hour[1])}).'
        ),
        (
            f'{busiest_weekday[0]} is the busiest weekday ({_one_decimal(busiest_weekday[1])}).'
            f' {quietest_weekday[0]} is the quietest ({_one_decimal(quietest_weekday[1])}).'
        ),
        (
            f'{busiest_month[0]} is the busiest month ({_one_decimal(busiest_month[1])}).'
            f' {quietest_month[0]} is the quietest ({_one_decimal(quietest_month[1])}).'
        ),
        '',
    ]
    lines.extend(_side_by_side(hour_pairs, weekday_pairs, month_pairs))
    return '\n'.join(lines)

def _side_cells(pairs, index):
    if index >= len(pairs):
        return ' | '
    label, value = pairs[index]
    return f'{label} | {_one_decimal(value)}'

def _side_by_side(hour_pairs, weekday_pairs, month_pairs):
    lines = [
        '| Hour | Avg flights | | Weekday | Avg peak | | Month | Avg peak |',
        '| --- | ---: | --- | --- | ---: | --- | --- | ---: |',
    ]
    rows = max(len(hour_pairs), len(weekday_pairs), len(month_pairs))
    for index in range(rows):
        lines.append(
            f'| {_side_cells(hour_pairs, index)}'
            f' | | {_side_cells(weekday_pairs, index)}'
            f' | | {_side_cells(month_pairs, index)} |'
        )
    return lines

def chart_city(name):
    label = sankey_label(name)
    label = re.sub(r'\s*\([^)]*\)', '', label).strip()
    return label or 'Unknown'

def cities_in_title(name):
    cities = []
    for part in re.split(r'\s*,\s*', str(name)):
        city = chart_city(part)
        if city in ('', 'Unknown', 'Tallinn') or city in cities:
            continue
        cities.append(city)
    return cities

def destination_counts(chart_df):
    counts = {}
    for title in chart_df['flight_title'].fillna(''):
        for city in cities_in_title(title):
            counts[city] = counts.get(city, 0) + 1
    if not counts:
        return pd.Series(dtype='int64')
    return pd.Series(counts).sort_values(ascending=False)

def scrape_span(chart_df):
    parsed = pd.to_datetime(chart_df['date'])
    start = parsed.min()
    end = parsed.max()
    years = max((end - start).days, 1) / 365.25
    return start.date(), years

def since_label(start):
    months = ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec')
    return f'{start.day} {months[start.month - 1]} {start.year}'

def destination_chart(counts, years, width=24):
    if counts.empty:
        return 'No destinations yet.'
    peak = int(counts.iloc[0]) or 1
    days = years * 365.25
    weeks = days / 7
    months = years * 12
    name_width = max(len(str(name)) for name in counts.index)
    lines = ['```']
    for name, count in counts.items():
        total = int(count)
        bar = '█' * max(1, round(width * total / peak))
        lines.append(
            f'{name:<{name_width}}  {total:>5}'
            f'  {total / days:>4.1f}/day'
            f'  {total / weeks:>5.1f}/wk'
            f'  {total / months:>6.1f}/mo'
            f'  {total / years:>6.1f}/yr'
            f'  {bar}'
        )
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
        'terminal_history': terminal_history(chart_df, today),
        'since_date': since_label(started),
        'destination_chart': destination_chart(
            destination_df.set_index('flight_title')['count'],
            years,
        ),
    }

    generate_readme('readme_template.yml', chart_data, 'README.md')

if __name__ == "__main__":
    main()
