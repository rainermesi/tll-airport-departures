import tempfile
import unittest
from pathlib import Path

import requests

import departure_scraper

FIXTURE = Path(__file__).parent / 'fixtures' / 'departures_fragment.html'
PAGE_HTML = (
    '<div class="container js-flights" data-id="4533" '
    'data-type="" data-filter="" data-lang="et"></div>'
)


class Response:
    def __init__(self, text='', json_data=None, status=200):
        self.text = text
        self._json = json_data
        self.status_code = status

    def raise_for_status(self):
        if self.status_code >= 400:
            raise requests.HTTPError(self.status_code)

    def json(self):
        return self._json


class ParseDeparturesTest(unittest.TestCase):
    def test_parser_keeps_today_cards_including_history(self):
        html = FIXTURE.read_text(encoding='utf-8')
        rows = departure_scraper.parse_departures(html, '2026-10-26')
        self.assertEqual(rows, [
            ['AY 1028', 'Helsingi', 'Finnair', '21:45', '21:55', '2026-10-26'],
            ['BT 362', 'Riia', 'Air Baltic Corporation', '05:40', 'N/A', '2026-10-26'],
        ])

    def test_missing_fields_become_na(self):
        html = '<li class="flights-list__item departures-today"></li>'
        rows = departure_scraper.parse_departures(html, '2026-10-26')
        self.assertEqual(rows, [['N/A', 'N/A', 'N/A', 'N/A', 'N/A', '2026-10-26']])


class FlightsQueryParamsTest(unittest.TestCase):
    def test_reads_js_flights_dataset(self):
        self.assertEqual(
            departure_scraper.flights_query_params(PAGE_HTML),
            {'id': '4533', 'type': '', 'filter': '', 'lang': 'et'},
        )

    def test_missing_block_raises(self):
        with self.assertRaises(ValueError):
            departure_scraper.flights_query_params('<div></div>')


class LoadDepartureHtmlTest(unittest.TestCase):
    def setUp(self):
        self.cards_html = FIXTURE.read_text(encoding='utf-8')

    def test_api_html_wins_without_selenium(self):
        calls = []

        def get(url, headers=None, timeout=None, params=None):
            calls.append((url, params))
            if url == departure_scraper.FLIGHTS_PAGE_URL:
                return Response(text=PAGE_HTML)
            return Response(json_data={'html': self.cards_html})

        def fetch_selenium(url):
            raise AssertionError('selenium should not run')

        html = departure_scraper.load_departure_html(get=get, fetch_selenium=fetch_selenium)
        self.assertIn('AY 1028', html)
        self.assertEqual(calls[1][1]['id'], '4533')
        self.assertEqual(calls[1][1]['lang'], 'et')

    def test_empty_api_falls_through_to_selenium(self):
        def get(url, headers=None, timeout=None, params=None):
            if url == departure_scraper.FLIGHTS_PAGE_URL:
                return Response(text=PAGE_HTML)
            return Response(json_data={'html': '<ul></ul>'})

        seen = []

        def fetch_selenium(url):
            seen.append(url)
            return self.cards_html

        html = departure_scraper.load_departure_html(get=get, fetch_selenium=fetch_selenium)
        self.assertEqual(seen, [departure_scraper.FLIGHTS_PAGE_URL])
        self.assertIn('BT 362', html)

    def test_api_error_falls_through_to_selenium(self):
        def get(url, headers=None, timeout=None, params=None):
            raise requests.ConnectionError('cloudflare')

        html = departure_scraper.load_departure_html(
            get=get,
            fetch_selenium=lambda url: self.cards_html,
        )
        self.assertIn('Helsingi', html)

    def test_both_sources_empty_exits_without_rows(self):
        def get(url, headers=None, timeout=None, params=None):
            if url == departure_scraper.FLIGHTS_PAGE_URL:
                return Response(text=PAGE_HTML)
            return Response(json_data={'html': '<ul></ul>'})

        with self.assertRaises(SystemExit) as raised:
            departure_scraper.load_departure_html(
                get=get,
                fetch_selenium=lambda url: '<ul></ul>',
            )
        self.assertEqual(raised.exception.code, 1)

    def test_selenium_none_exits(self):
        def get(url, headers=None, timeout=None, params=None):
            raise TimeoutError('timed out')

        with self.assertRaises(SystemExit):
            departure_scraper.load_departure_html(get=get, fetch_selenium=lambda url: None)


class WriteCsvTest(unittest.TestCase):
    def test_writes_header_and_rows(self):
        with tempfile.TemporaryDirectory() as directory:
            path = departure_scraper.write_departures_csv(
                [['AY 1028', 'Helsingi', 'Finnair', '21:45', '21:55', '2026-10-26']],
                '2026-10-26',
                directory=directory,
            )
            text = Path(path).read_text(encoding='utf-8')
            self.assertTrue(path.endswith('departures_log_2026-10-26.csv'))
            self.assertEqual(
                text,
                'flight_number,flight_title,service_provider_name,scheduled_time,departure_time,date\n'
                'AY 1028,Helsingi,Finnair,21:45,21:55,2026-10-26\n',
            )


if __name__ == '__main__':
    unittest.main()
