from pathlib import Path
import math
import re

import pandas as pd

from destinations import normalize_destination

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

def get_chart_values(merged_df):
    chart_df = rows_for_charts(merged_df)
    result_1 = chart_df.groupby(chart_df['date']).agg(
        count = ('date','size'),
        unique_destinations = ('flight_title','nunique')
    ).reset_index()
    result_1 = result_1.sort_values('date').tail(CHART_DAYS)

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


def main():
    chart_values_df, sankey_values_df = get_chart_values(merge_csv_files(get_data_path()))
    chart_dates = create_chart_dates(chart_values_df, 'date')
    chart_counts = chart_values_df['count'].to_list()
    chart_unique_destinations = chart_values_df['unique_destinations'].to_list()
    chart_ymax = max(chart_counts) + math.ceil(max(chart_counts) / 10)
    sankey_csv = sankey_values_df.to_csv(index=False, header=False)

    chart_data = {
        'title': 'Departures by day',
        'x_axis': chart_dates,
        'y_axis': '# departures',
        'bar_values': chart_counts,
        'line_values': chart_unique_destinations,
        'ymax': chart_ymax,
        'sankey_data': sankey_csv
    }

    generate_readme('readme_template.yml', chart_data, 'README.md')

if __name__ == "__main__":
    main()
