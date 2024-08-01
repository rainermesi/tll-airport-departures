import requests
from bs4 import BeautifulSoup
from datetime import datetime
import csv

url = "https://airport.ee/lennuinfo/"

headers = {
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "accept-language": "en-US,en;q=0.9",
    "cache-control": "max-age=0",
    "upgrade-insecure-requests": "1",
    "referer": "https://www.google.com/"
}

response = requests.get(url, headers=headers)

soup = BeautifulSoup(response.text, 'html.parser')

flights_list_items = soup.find_all('li', class_='flights-list__item departures-today')

# Extract and save info from each list item to a list object
departures_list = []
log_date = datetime.now().strftime('%Y-%m-%d')

for li in flights_list_items:
    flight_numbers = li.find('span', class_='card-flight__flight-numbers')
    service_providers = li.find('span', class_='card-flight__service-providers')
    flight_time = li.find('span', class_='card-flight__time')
    depart_time = li.find('em', class_='card-flight__tag card-flight__tag--departed')
    try:
        flight_title = li.find('div', class_='card-flight__content').find('h2', class_='card-flight__title')
    except:
        flight_title = 'N/A'
    flight_numbers_text = flight_numbers.get_text(strip=True) if flight_numbers else 'N/A'
    flight_time_text = flight_time.get_text(strip=True) if flight_time else 'N/A'
    depart_time_text = depart_time.get_text(strip=True).split(' ')[1] if depart_time else 'N/A'
    service_providers_text = service_providers.get_text(strip=True) if service_providers else 'N/A'
    try:
        flight_title_text = flight_title.get_text(strip=True)
    except:
        flight_title_text = 'N/A'

    departures_list.append([
        flight_numbers_text,
        flight_title_text,
        service_providers_text,
        flight_time_text,
        depart_time_text,
        log_date
        ])


with open(f'data/departures_log_{log_date}.csv', 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(['flight_number','flight_title','service_provider_name','scheduled_time','departure_time','date'])
    csvwriter.writerows(departures_list)
