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


if __name__ == '__main__':
    unittest.main()
