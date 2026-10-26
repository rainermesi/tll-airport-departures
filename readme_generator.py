from pathlib import Path
import math
import re

import pandas as pd

from destinations import normalize_destination
from hall_crowd import morning_crowd

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

def crowd_by_date(chart_df):
    points = []
    for date, group in chart_df.groupby('date', sort=True):
        value = morning_crowd(group.to_dict('records'))
        if value is None:
            continue
        points.append((str(date), round(value, 2)))
    return points

def get_chart_values(merged_df):
    chart_df = rows_for_charts(merged_df)
    result_1 = daily_counts(chart_df).tail(CHART_DAYS)

    result_2 = chart_df.groupby(chart_df['flight_title']).size().reset_index(name='count')
    result_2.insert(0,'source','Tallinn')
    result_2['flight_title'] = result_2['flight_title'].str.replace('õ', 'o', flags=re.IGNORECASE, regex=True)
    result_2['flight_title'] = result_2['flight_title'].str.replace('ä', 'a', flags=re.IGNORECASE, regex=True)
    result_2['flight_title'] = result_2['flight_title'].str.replace('ö', 'o', flags=re.IGNORECASE, regex=True)
    result_2['flight_title'] = result_2['flight_title'].str.replace('ü', 'u', flags=re.IGNORECASE, regex=True)
    result_2['flight_title'] = result_2['flight_title'].str.replace('é', 'e', flags=re.IGNORECASE, regex=True)
    result_2['flight_title'] = result_2['flight_title'].str.replace('/', '', flags=re.IGNORECASE, regex=True)
    result_2['flight_title'] = result_2['flight_title'].str.replace('š', 's', flags=re.IGNORECASE, regex=True)

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
    raw_date_list = [date for date in dataframe[column]]
    string_date_list = ', '.join(f'"{date}"' for date in raw_date_list)
    return string_date_list


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
    crowd = crowd_by_date(chart_df)[-CHART_DAYS:]
    _chart_values_df, sankey_values_df = get_chart_values(merged)
    sankey_csv = sankey_values_df.to_csv(index=False, header=False)
    crowd_values = [value for _date, value in crowd]

    chart_data = {
        'title': 'Departures by day',
        'x_axis': create_chart_dates(recent, 'date'),
        'y_axis': '# departures',
        'bar_values': recent['count'].to_list(),
        'line_values': recent['unique_destinations'].to_list(),
        'ymax': chart_limit(recent['count'].to_list()),
        'quarter_x': ', '.join(f'"{quarter}"' for quarter in quarters['quarter']),
        'quarter_bar': number_list(quarters['avg_departures'], 1),
        'quarter_line': number_list(quarters['avg_destinations'], 1),
        'quarter_ymax': chart_limit(quarters['avg_departures'].to_list()),
        'crowd_x': ', '.join(f'"{date}"' for date, _value in crowd),
        'crowd_bar': number_list(crowd_values, 2),
        'crowd_ymax': chart_limit(crowd_values),
        'sankey_data': sankey_csv
    }

    generate_readme('readme_template.yml', chart_data, 'README.md')

if __name__ == "__main__":
    main()
