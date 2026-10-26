import tempfile
import unittest
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

import requests

import departure_scraper

FIXTURE = Path(__file__).parent / 'fixtures' / 'departures_fragment.html'
PAGE_HTML = (
    '<div class="container js-flights" data-id="4533" '
    'data-type="" data-filter="" data-lang="et"></div>'
)
NOW = datetime(2026, 10, 26, 22, 0, tzinfo=ZoneInfo('Europe/Tallinn'))


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


def cards_html(count, board='departures-today', title='Riia'):
    items = []
    for index in range(count):
        items.append(
            f'<li class="flights-list__item {board}">'
            f'<span class="card-flight__flight-numbers">BT {index}</span>'
            f'<span class="card-flight__time">05:40</span>'
            f'<div class="card-flight__content"><h2 class="card-flight__title">{title}</h2></div>'
            f'<span class="card-flight__service-providers">Air Baltic</span>'
            f'</li>'
        )
    return '<ul>' + ''.join(items) + '</ul>'


def api_get(html):
    def get(url, headers=None, timeout=None, params=None):
        if url == departure_scraper.FLIGHTS_PAGE_URL:
            return Response(text=PAGE_HTML)
        return Response(json_data={'html': html})
    return get


class ParseDeparturesTest(unittest.TestCase):
    def test_parser_keeps_status_actual_time_and_tomorrow(self):
        html = FIXTURE.read_text(encoding='utf-8')
        rows = departure_scraper.parse_departures(html, '2026-10-26')
        self.assertEqual(rows, [
            {
                'flight_number': 'AY 1028',
                'flight_title': 'Helsingi',
                'service_provider_name': 'Finnair',
                'scheduled_time': '21:45',
                'live_time': '21:55',
                'departure_time': '21:55',
                'date': '2026-10-26',
                'status': 'departed|delayed',
                'board': 'today',
            },
            {
                'flight_number': 'BT 362',
                'flight_title': 'Amsterdam',
                'service_provider_name': 'Air Baltic Corporation',
                'scheduled_time': '05:40',
                'live_time': 'N/A',
                'departure_time': 'N/A',
                'date': '2026-10-26',
                'status': 'N/A',
                'board': 'today',
            },
            {
                'flight_number': 'FR 123',
                'flight_title': 'London (Gatwick)',
                'service_provider_name': 'Ryanair',
                'scheduled_time': '06:10',
                'live_time': 'N/A',
                'departure_time': 'N/A',
                'date': '2026-10-27',
                'status': 'N/A',
                'board': 'tomorrow',
            },
        ])

    def test_heading_without_flight_number_is_skipped(self):
        html = '<li class="flights-list__item departures-today"><h2>26. oktoober</h2></li>'
        self.assertEqual(departure_scraper.parse_departures(html, '2026-10-26'), [])


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
    def test_api_html_wins_without_selenium_when_board_is_full(self):
        html = cards_html(departure_scraper.MIN_TODAY_DEPARTURES)

        def fetch_selenium(url):
            raise AssertionError('selenium should not run')

        loaded = departure_scraper.load_departure_html(
            get=api_get(html),
            fetch_selenium=fetch_selenium,
        )
        self.assertIn('BT 0', loaded)

    def test_short_api_falls_through_to_selenium(self):
        seen = []

        def fetch_selenium(url):
            seen.append(url)
            return cards_html(departure_scraper.MIN_TODAY_DEPARTURES, title='Genf')

        loaded = departure_scraper.load_departure_html(
            get=api_get(FIXTURE.read_text(encoding='utf-8')),
            fetch_selenium=fetch_selenium,
        )
        self.assertEqual(seen, [departure_scraper.FLIGHTS_PAGE_URL])
        self.assertIn('Genf', loaded)

    def test_api_error_falls_through_to_selenium(self):
        def get(url, headers=None, timeout=None, params=None):
            raise requests.ConnectionError('cloudflare')

        loaded = departure_scraper.load_departure_html(
            get=get,
            fetch_selenium=lambda url: cards_html(departure_scraper.MIN_TODAY_DEPARTURES),
        )
        self.assertIn('BT 0', loaded)

    def test_both_sources_empty_exits(self):
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


class RetryTest(unittest.TestCase):
    def test_short_board_retries_then_exits_without_writing(self):
        sleeps = []
        with tempfile.TemporaryDirectory() as directory:
            with self.assertRaises(SystemExit):
                departure_scraper.scrape_with_retries(
                    get=api_get(cards_html(2)),
                    fetch_selenium=lambda url: cards_html(2),
                    sleep=sleeps.append,
                    now=NOW,
                    attempts=3,
                )
            self.assertEqual(sleeps, [departure_scraper.RETRY_WAIT_SECONDS, departure_scraper.RETRY_WAIT_SECONDS])
            self.assertEqual(list(Path(directory).glob('*.csv')), [])

    def test_full_board_returns_today_and_tomorrow(self):
        html = cards_html(15) + cards_html(1, board='departures-tomorrow', title='Genf')
        log_date, rows = departure_scraper.scrape_with_retries(
            get=api_get(html),
            fetch_selenium=lambda url: (_ for _ in ()).throw(AssertionError('selenium')),
            sleep=lambda seconds: (_ for _ in ()).throw(AssertionError('sleep')),
            now=NOW,
            attempts=1,
        )
        self.assertEqual(log_date.isoformat(), '2026-10-26')
        self.assertEqual(sum(row['board'] == 'today' for row in rows), 15)
        tomorrow = [row for row in rows if row['board'] == 'tomorrow']
        self.assertEqual(tomorrow[0]['flight_title'], 'Genf')
        self.assertEqual(tomorrow[0]['date'], '2026-10-27')


class WriteCsvTest(unittest.TestCase):
    def test_writes_header_and_rows(self):
        row = {
            'flight_number': 'AY 1028',
            'flight_title': 'Helsingi',
            'service_provider_name': 'Finnair',
            'scheduled_time': '21:45',
            'departure_time': '21:55',
            'date': '2026-10-26',
            'status': 'departed|delayed',
            'board': 'today',
        }
        with tempfile.TemporaryDirectory() as directory:
            path = departure_scraper.write_departures_csv([row], '2026-10-26', directory=directory)
            text = Path(path).read_text(encoding='utf-8')
            self.assertTrue(path.endswith('departures_log_2026-10-26.csv'))
            self.assertEqual(
                text,
                'flight_number,flight_title,service_provider_name,scheduled_time,first_seen_time,estimated_time,departure_time,date,status,board\n'
                'AY 1028,Helsingi,Finnair,21:45,N/A,N/A,21:55,2026-10-26,departed|delayed,today\n',
            )


class MergeFlightsTest(unittest.TestCase):
    def test_first_seen_time_is_kept_and_actual_is_filled_later(self):
        first = departure_scraper._new_record({
            'flight_number': 'XQ 499',
            'flight_title': 'Antalya',
            'service_provider_name': 'SunExpress',
            'scheduled_time': '06:45',
            'live_time': 'N/A',
            'date': '2026-10-27',
            'status': 'N/A',
            'board': 'tomorrow',
        })
        self.assertEqual(first['first_seen_time'], '06:45')
        self.assertEqual(first['departure_time'], 'N/A')

        revised = departure_scraper._apply_update(first, {
            'flight_number': 'XQ 499',
            'flight_title': 'Antalya',
            'service_provider_name': 'SunExpress',
            'scheduled_time': '06:45',
            'live_time': '07:05',
            'date': '2026-10-27',
            'status': 'estimated|delayed',
            'board': 'today',
        })
        self.assertEqual(revised['first_seen_time'], '06:45')
        self.assertEqual(revised['estimated_time'], '07:05')
        self.assertEqual(revised['departure_time'], 'N/A')

        departed = departure_scraper._apply_update(revised, {
            'flight_number': 'XQ 499',
            'flight_title': 'Antalya',
            'service_provider_name': 'SunExpress',
            'scheduled_time': '06:45',
            'live_time': '07:10',
            'date': '2026-10-27',
            'status': 'departed|delayed',
            'board': 'today',
        })
        self.assertEqual(departed['first_seen_time'], '06:45')
        self.assertEqual(departed['estimated_time'], '07:05')
        self.assertEqual(departed['departure_time'], '07:10')

    def test_already_departed_on_first_sight_has_no_baseline(self):
        row = departure_scraper._new_record({
            'flight_number': 'AY 1028',
            'flight_title': 'Helsingi',
            'service_provider_name': 'Finnair',
            'scheduled_time': '21:45',
            'live_time': '21:55',
            'date': '2026-10-26',
            'status': 'departed|delayed',
            'board': 'today',
        })
        self.assertEqual(row['first_seen_time'], 'N/A')
        self.assertEqual(row['departure_time'], '21:55')

    def test_old_rows_do_not_gain_a_retroactive_baseline(self):
        old = {
            'flight_number': 'BT 362',
            'flight_title': 'Riia',
            'service_provider_name': 'Air Baltic Corporation',
            'scheduled_time': '05:40',
            'departure_time': 'N/A',
            'date': '2026-10-26',
        }
        merged = departure_scraper.merge_flights([old], [{
            'flight_number': 'BT 362',
            'flight_title': 'Riia',
            'service_provider_name': 'Air Baltic Corporation',
            'scheduled_time': '05:40',
            'live_time': '05:44',
            'date': '2026-10-26',
            'status': 'departed',
            'board': 'today',
        }])
        self.assertEqual(merged[0]['first_seen_time'], 'N/A')
        self.assertEqual(merged[0]['estimated_time'], 'N/A')
        self.assertEqual(merged[0]['departure_time'], '05:44')

    def test_save_writes_tomorrow_into_tomorrows_file(self):
        scraped = [{
            'flight_number': 'XQ 499',
            'flight_title': 'Antalya',
            'service_provider_name': 'SunExpress',
            'scheduled_time': '06:45',
            'live_time': 'N/A',
            'date': '2026-10-27',
            'status': 'N/A',
            'board': 'tomorrow',
        }]
        with tempfile.TemporaryDirectory() as directory:
            paths = departure_scraper.save_scraped_flights(scraped, directory=directory)
            self.assertEqual(len(paths), 1)
            self.assertTrue(paths[0].endswith('departures_log_2026-10-27.csv'))
            stored = departure_scraper.read_departures_csv(paths[0])
            self.assertEqual(stored[0]['first_seen_time'], '06:45')


if __name__ == '__main__':
    unittest.main()
