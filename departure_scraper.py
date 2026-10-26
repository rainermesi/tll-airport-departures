from bs4 import BeautifulSoup
from datetime import datetime
import csv
import logging
import os

import requests

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
CSV_HEADER = [
    'flight_number',
    'flight_title',
    'service_provider_name',
    'scheduled_time',
    'departure_time',
    'date',
]


def departure_cards(soup):
    # Cards that have already departed also carry departures-history.
    # Beautiful Soup 4.13+ treats a multi-class class_ string as an exact
    # class list, so select on both classes keeps those cards.
    return soup.select('li.flights-list__item.departures-today')


def parse_departures(html, log_date):
    soup = BeautifulSoup(html, 'html.parser')
    flights_list_items = departure_cards(soup)
    logging.info(f'Found {len(flights_list_items)} departure items.')

    departures_list = []
    for li in flights_list_items:
        flight_numbers = li.find('span', class_='card-flight__flight-numbers')
        service_providers = li.find('span', class_='card-flight__service-providers')
        flight_time = li.find('span', class_='card-flight__time')
        depart_time = li.find('em', class_='card-flight__tag card-flight__tag--departed')
        try:
            flight_title = li.find('div', class_='card-flight__content').find('h2', class_='card-flight__title')
        except Exception:
            flight_title = 'N/A'
        flight_numbers_text = flight_numbers.get_text(strip=True) if flight_numbers else 'N/A'
        flight_time_text = flight_time.get_text(strip=True) if flight_time else 'N/A'
        depart_time_text = depart_time.get_text(strip=True).split(' ')[1] if depart_time else 'N/A'
        service_providers_text = service_providers.get_text(strip=True) if service_providers else 'N/A'
        try:
            flight_title_text = flight_title.get_text(strip=True)
        except Exception:
            flight_title_text = 'N/A'

        departures_list.append([
            flight_numbers_text,
            flight_title_text,
            service_providers_text,
            flight_time_text,
            depart_time_text,
            log_date,
        ])
    return departures_list


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
    try:
        html = fetch_flights_api_html(get)
        cards = departure_cards(BeautifulSoup(html, 'html.parser'))
        if cards:
            logging.info('Using flights API HTML (%s departures-today cards)', len(cards))
            return html
        logging.warning('Flights API returned no departures-today cards')
    except Exception as exc:
        logging.warning('Flights API fetch failed: %s', exc)

    logging.info('Falling back to Selenium')
    if fetch_selenium is None:
        from selenium_fetch import fetch_page_html
        fetch_selenium = fetch_page_html
    html = fetch_selenium(FLIGHTS_PAGE_URL)
    if not html:
        logging.error('Selenium returned no HTML')
        raise SystemExit(1)
    cards = departure_cards(BeautifulSoup(html, 'html.parser'))
    if not cards:
        logging.error('No departures-today cards from API or Selenium')
        raise SystemExit(1)
    logging.info('Using Selenium HTML (%s departures-today cards)', len(cards))
    return html


def departures_log_path(log_date, directory='data/logs'):
    return os.path.join(directory, f'departures_log_{log_date}.csv')


def write_departures_csv(rows, log_date, directory='data/logs'):
    path = departures_log_path(log_date, directory)
    with open(path, 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(CSV_HEADER)
        csvwriter.writerows(rows)
    return path


def main():
    html = load_departure_html()
    log_date = datetime.now().strftime('%Y-%m-%d')
    rows = parse_departures(html, log_date)
    if not rows:
        logging.error('No departures to write')
        raise SystemExit(1)
    path = write_departures_csv(rows, log_date)
    logging.info('Wrote %s rows to %s', len(rows), path)


if __name__ == '__main__':
    main()
