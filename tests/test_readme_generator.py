from datetime import date
import unittest

import pandas as pd

import readme_generator


class RenderTemplateTest(unittest.TestCase):
    def test_braces_in_values_are_left_alone(self):
        rendered = readme_generator.render_template(
            'title {title}\n{sankey_data}',
            {'title': 'Departures by day', 'sankey_data': 'Tallinn,Genf{extra},1\n'},
        )
        self.assertEqual(rendered, 'title Departures by day\nTallinn,Genf{extra},1\n')


class ChartWindowTest(unittest.TestCase):
    def test_chart_uses_last_90_days_and_skips_tomorrow_board(self):
        dates = [f'2026-01-{day:02d}' for day in range(1, 32)]
        dates += [f'2026-02-{day:02d}' for day in range(1, 29)]
        dates += [f'2026-03-{day:02d}' for day in range(1, 32)]
        dates += [f'2026-04-{day:02d}' for day in range(1, 11)]
        rows = []
        for date in dates:
            rows.append({'date': date, 'flight_title': 'Amsterdam (Schiphol)', 'board': 'today'})
        rows.append({'date': '2026-04-09', 'flight_title': 'Geneva', 'board': 'today'})
        rows.append({'date': '2026-04-10', 'flight_title': 'Geneva', 'board': 'tomorrow'})
        frame = pd.DataFrame(rows)
        frame['flight_title'] = frame['flight_title'].map(
            __import__('destinations').normalize_destination
        )
        daily, sankey = readme_generator.get_chart_values(frame)
        self.assertEqual(len(daily), readme_generator.CHART_DAYS)
        quarters = readme_generator.quarter_averages(
            readme_generator.daily_counts(
                readme_generator.rows_for_charts(frame)
            )
        )
        self.assertEqual(list(quarters['quarter']), ['2026 Q1', '2026 Q2'])
        self.assertEqual(daily['date'].iloc[0], '2026-01-11')
        self.assertEqual(daily['date'].iloc[-1], '2026-04-10')
        self.assertEqual(int(daily.loc[daily['date'] == '2026-04-09', 'count'].iloc[0]), 2)
        self.assertEqual(int(daily.loc[daily['date'] == '2026-04-10', 'count'].iloc[0]), 1)
        titles = set(sankey['flight_title'])
        self.assertIn('Amsterdam', titles)
        self.assertIn('Genf', titles)
        self.assertNotIn('Geneva', titles)
        labels = readme_generator.sparse_date_labels(list(daily['date']))
        self.assertIn('"11.01"', labels)
        self.assertGreater(labels.count('" "'), 70)

    def test_destination_chart_groups_airports_and_scales_the_bar(self):
        frame = pd.DataFrame([
            {'date': '2026-10-01', 'flight_title': 'Gdańsk', 'board': 'today'},
            {'date': '2026-10-01', 'flight_title': 'Zürich', 'board': 'today'},
            {'date': '2026-10-01', 'flight_title': 'Tallinn (Lennart Meri)', 'board': 'today'},
            {'date': '2026-10-01', 'flight_title': 'London (Gatwick)', 'board': 'today'},
            {'date': '2026-10-02', 'flight_title': 'London (Luton)', 'board': 'today'},
            {'date': '2026-10-03', 'flight_title': 'London (Stansted)', 'board': 'today'},
            {'date': '2026-10-01', 'flight_title': 'Stockholm (Arlanda)', 'board': 'today'},
            {'date': '2026-10-02', 'flight_title': 'Stockholm (Bromma)', 'board': 'today'},
        ])
        _daily, destinations = readme_generator.get_chart_values(frame)
        counts = dict(zip(destinations['flight_title'], destinations['count']))
        self.assertEqual(counts['London'], 3)
        self.assertEqual(counts['Stockholm'], 2)
        self.assertNotIn('Tallinn', counts)
        self.assertIn('Gdansk', counts)
        chart = readme_generator.destination_chart(
            destinations.set_index('flight_title')['count'],
            years=2,
        )
        london = next(line for line in chart.splitlines() if line.startswith('London'))
        gdansk = next(line for line in chart.splitlines() if line.startswith('Gdansk'))
        self.assertGreater(london.count('█'), gdansk.count('█'))
        self.assertIn('1.5/yr', london)

    def test_forecast_uses_tomorrow_when_it_is_already_logged(self):
        frame = pd.DataFrame([
            {'date': '2026-10-26', 'flight_title': 'Riia', 'scheduled_time': '12:00', 'flight_number': 'BT 1', 'board': 'today'},
            {'date': '2026-10-27', 'flight_title': 'Antalya', 'scheduled_time': '06:45', 'flight_number': 'XQ 1', 'board': 'tomorrow'},
        ])
        text = readme_generator.terminal_forecast(frame, date(2026, 10, 26))
        self.assertIn('**2026-10-27**', text)
        self.assertIn('| 05:00 |', text)


if __name__ == '__main__':
    unittest.main()
