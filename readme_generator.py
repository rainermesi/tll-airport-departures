from pathlib import Path
import pandas as pd

def get_data_path():
    data_path = Path('/data')
    csv_list = list(data_path.glob('*.csv'))
    return csv_list

def merge_csv_files(csv_files):
    dataframes = [pd.read_csv(file) for file in csv_files]
    merged_df = pd.concat(dataframes, ignore_index=True)
    return merged_df

def get_chart_values(merged_df):
    result = merged_df.groupby(merged_df['date']).size().reset_index(name='count')
    return result

def generate_readme(template_path, data, output_path):
    with open(template_path,'r') as template_file:
        template = template_file.read()

    readme_content = template.format(**data)

    with open(output_path, 'w') as output_file:
        output_file.write(readme_content)

def main():
    chart_values_df = get_chart_values(merge_csv_files(get_data_path()))
    chart_dates = ', '.join(f'"{date}"' for date in chart_values_df['date'])
    chart_counts = chart_values_df['count'].to_list()

    chart_data = {
        'title': 'Departures by day',
        'x_axis': chart_dates,
        'y_axis': '# departures',
        'bar_values': chart_counts,
        'line_values': chart_counts
    }

    generate_readme('/workspaces/tll-airport-departures/readme_template.yml', chart_data, '/workspaces/tll-airport-departures/README.md')

if __name__ == "__main__":
    main()
