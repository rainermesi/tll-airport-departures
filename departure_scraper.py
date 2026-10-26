from bs4 import BeautifulSoup
from datetime import datetime, timedelta
from zoneinfo import ZoneInfo
import csv
import logging
import os
import re
import time

import requests

from destinations import normalize_destination

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

FLIGHTS_PAGE_URL = 'https://airport.ee/lennuinfo/'
FLIGHTS_API_URL = 'https://airport.ee/wp-json/airport/v1/flights'
REQUEST_TIMEOUT = 30
USER_AGENT = (
    'Mozilla/5.0 (compatible; tll-airport-departures/1.0; +https://github.com/rainermesi/tll-airport-departures)'
)
TALLINN = ZoneInfo('Europe/Tallinn')
MIN_TODAY_DEPARTURES = 15
MAX_ATTEMPTS = 3
RETRY_WAIT_SECONDS = 20
CSV_HEADER = [
    'flight_number',
    'flight_title',
    'service_provider_name',
    'scheduled_time',
    'departure_time',
    'date',
    'status',
    'board',
]
TAG_PREFIX = 'card-flight__tag--'
TAG_SKIP = {'departures', 'arrivals'}
TIME_RE = re.compile(r'\d{1,2}:\d{2}')


def departure_cards(soup, board='today'):
    # Cards that have already departed also carry departures-history.
    # Beautiful Soup 4.13+ treats a multi-class class_ string as an exact
    # class list, so select on both classes keeps those cards.
    return soup.select(f'li.flights-list__item.departures-{board}')


def today_card_count(html):
    if not html:
        return 0
    soup = BeautifulSoup(html, 'html.parser')
    return sum(
        1 for li in departure_cards(soup, 'today')
        if li.find('span', class_='card-flight__flight-numbers')
    )


def _text(node):
    return node.get_text(strip=True) if node else 'N/A'


def _clock(text):
    if not text:
        return None
    match = TIME_RE.search(text)
    return match.group(0) if match else None


def card_status(li):
    tags = []
    for em in li.select('em.card-flight__tag'):
        for class_name in em.get('class', []):
            if not class_name.startswith(TAG_PREFIX):
                continue
            name = class_name[len(TAG_PREFIX):]
            if name in TAG_SKIP or name in tags:
                continue
            tags.append(name)
    return '|'.join(tags) if tags else 'N/A'


def scheduled_time(li):
    old = li.select_one('.card-flight__time--old')
    if old:
        return _text(old)
    current = li.select_one('span.card-flight__time') or li.select_one('ins.card-flight__time')
    return _text(current)


def actual_time(li):
    updated = li.select_one('ins.card-flight__time')
    if updated:
        return _text(updated)
    for class_name in ('departed', 'estimated', 'closed'):
        tag = li.select_one(f'em.card-flight__tag--{class_name}')
        clock = _clock(_text(tag) if tag else '')
        if clock:
            return clock
    return 'N/A'


def parse_departures(html, today, tomorrow=None):
    if isinstance(today, str):
        today = datetime.strptime(today, '%Y-%m-%d').date()
    if tomorrow is None:
        tomorrow = today + timedelta(days=1)
    elif isinstance(tomorrow, str):
        tomorrow = datetime.strptime(tomorrow, '%Y-%m-%d').date()

    soup = BeautifulSoup(html, 'html.parser')
    departures = []
    for board, flight_date in (('today', today), ('tomorrow', tomorrow)):
        cards = departure_cards(soup, board)
        logging.info('Found %s departures-%s items.', len(cards), board)
        for li in cards:
            flight_numbers = li.find('span', class_='card-flight__flight-numbers')
            if not flight_numbers or not flight_numbers.get_text(strip=True):
                continue
            service_providers = li.find('span', class_='card-flight__service-providers')
            try:
                flight_title = li.find('div', class_='card-flight__content').find('h2', class_='card-flight__title')
                flight_title_text = flight_title.get_text(strip=True)
            except Exception:
                flight_title_text = 'N/A'
            departures.append({
                'flight_number': flight_numbers.get_text(strip=True),
                'flight_title': normalize_destination(flight_title_text),
                'service_provider_name': _text(service_providers),
                'scheduled_time': scheduled_time(li),
                'departure_time': actual_time(li),
                'date': flight_date.isoformat(),
                'status': card_status(li),
                'board': board,
            })
    return departures


def flights_query_params(page_html):
    soup = BeautifulSoup(page_html, 'html.parser')
    node = soup.select_one('.js-flights')
    if node is None or not node.get('data-id'):
        raise ValueError('lennuinfo page has no .js-flights data-id')
    return {
        'id': node['data-id'],
        'type': node.get('data-type') or '',
        'filter': node.get('data-filter') or '',
        'lang': node.get('data-lang') or 'et',
    }


def fetch_flights_api_html(get=requests.get):
    headers = {'User-Agent': USER_AGENT}
    page = get(FLIGHTS_PAGE_URL, headers=headers, timeout=REQUEST_TIMEOUT)
    page.raise_for_status()
    params = flights_query_params(page.text)
    response = get(
        FLIGHTS_API_URL,
        params=params,
        headers={**headers, 'Accept': 'application/json'},
        timeout=REQUEST_TIMEOUT,
    )
    response.raise_for_status()
    payload = response.json()
    html = payload.get('html') if isinstance(payload, dict) else None
    if not html:
        raise ValueError('flights API response has no html')
    return html


def load_departure_html(get=requests.get, fetch_selenium=None):
    api_html = None
    try:
        api_html = fetch_flights_api_html(get)
        api_count = today_card_count(api_html)
        if api_count >= MIN_TODAY_DEPARTURES:
            logging.info('Using flights API HTML (%s departures-today cards)', api_count)
            return api_html
        logging.warning('Flights API returned %s departures-today cards', api_count)
    except Exception as exc:
        logging.warning('Flights API fetch failed: %s', exc)

    logging.info('Falling back to Selenium')
    if fetch_selenium is None:
        from selenium_fetch import fetch_page_html
        fetch_selenium = fetch_page_html
    html = fetch_selenium(FLIGHTS_PAGE_URL)
    selenium_count = today_card_count(html)
    if selenium_count >= MIN_TODAY_DEPARTURES:
        logging.info('Using Selenium HTML (%s departures-today cards)', selenium_count)
        return html
    if selenium_count == 0 and today_card_count(api_html) == 0:
        logging.error('No departures-today cards from API or Selenium')
        raise SystemExit(1)
    best = html if selenium_count >= today_card_count(api_html) else api_html
    logging.warning(
        'Best source has %s departures-today cards',
        today_card_count(best),
    )
    return best


def departures_log_path(log_date, directory='data/logs'):
    return os.path.join(directory, f'departures_log_{log_date}.csv')


def write_departures_csv(rows, log_date, directory='data/logs'):
    path = departures_log_path(log_date, directory)
    with open(path, 'w', newline='') as csvfile:
        csvwriter = csv.DictWriter(csvfile, fieldnames=CSV_HEADER)
        csvwriter.writeheader()
        csvwriter.writerows(rows)
    return path


def scrape_with_retries(
    get=requests.get,
    fetch_selenium=None,
    sleep=time.sleep,
    now=None,
    attempts=MAX_ATTEMPTS,
):
    now = now or datetime.now(TALLINN)
    if now.tzinfo is None:
        now = now.replace(tzinfo=TALLINN)
    today = now.astimezone(TALLINN).date()
    tomorrow = today + timedelta(days=1)
    last_count = 0
    for attempt in range(1, attempts + 1):
        try:
            html = load_departure_html(get=get, fetch_selenium=fetch_selenium)
            rows = parse_departures(html, today, tomorrow)
            last_count = sum(1 for row in rows if row['board'] == 'today')
            if last_count >= MIN_TODAY_DEPARTURES:
                return today, rows
            logging.warning(
                'Only %s departures today (attempt %s/%s); not writing a log',
                last_count,
                attempt,
                attempts,
            )
        except SystemExit:
            logging.warning('Scrape attempt %s/%s failed', attempt, attempts)
        if attempt < attempts:
            sleep(RETRY_WAIT_SECONDS)
    logging.error(
        'Giving up with %s departures today after %s attempts',
        last_count,
        attempts,
    )
    raise SystemExit(1)


def main():
    log_date, rows = scrape_with_retries()
    path = write_departures_csv(rows, log_date.isoformat())
    today_count = sum(1 for row in rows if row['board'] == 'today')
    logging.info('Wrote %s rows (%s today) to %s', len(rows), today_count, path)


if __name__ == '__main__':
    main()
