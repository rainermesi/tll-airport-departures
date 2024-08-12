from pathlib import Path
import pandas as pd
import math
import re

def get_data_path():
    data_path = Path('./data')
    csv_list = list(data_path.glob('*.csv'))
    return csv_list

def merge_csv_files(csv_files):
    dataframes = [pd.read_csv(file) for file in csv_files]
    merged_df = pd.concat(dataframes, ignore_index=True)
    merged_df['flight_title'] = merged_df['flight_title'].str.replace(r' \(.+\)', '', regex=True)
    return merged_df

def get_chart_values(merged_df):
    result_1 = merged_df.groupby(merged_df['date']).agg(
        count = ('date','size'),
        unique_destinations = ('flight_title','nunique')
    ).reset_index()

    result_2 = merged_df.groupby(merged_df['flight_title']).size().reset_index(name='count')
    result_2.insert(0,'source','Tallinn')
    result_2['flight_title'] = result_2['flight_title'].str.replace('õ', 'o', flags=re.IGNORECASE, regex=True)
    result_2['flight_title'] = result_2['flight_title'].str.replace('ä', 'a', flags=re.IGNORECASE, regex=True)
    result_2['flight_title'] = result_2['flight_title'].str.replace('ö', 'o', flags=re.IGNORECASE, regex=True)
    result_2['flight_title'] = result_2['flight_title'].str.replace('ü', 'u', flags=re.IGNORECASE, regex=True)

    return result_1, result_2

def generate_readme(template_path, data, output_path):
    with open(template_path,'r') as template_file:
        template = template_file.read()

    readme_content = template.format(**data)

    with open(output_path, 'w') as output_file:
        output_file.write(readme_content)

def create_chart_dates(dataframe, column):
    raw_date_list = [date for date in dataframe[column]]
    parsed_date_list = []
    first_dt = raw_date_list[0]
    last_dt = len(raw_date_list)
    for index, item in enumerate(len(raw_date_list)):
        if index == 0:
            output_date_list.append(first_dt)
        elif index == len(raw_date_list):
            output_date_list.append(last_dt)
        else:
            output_date_list.append('-')
    string_date_list = ', '.join(f'"{date}"' for date in parsed_date_list) 
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
