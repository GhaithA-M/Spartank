import requests
import json
from bs4 import BeautifulSoup

def fetch_html(url):
    response = requests.get(url)
    response.raise_for_status()  # Raises an HTTPError for bad responses
    return response.text

def parse_ok(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    rows = soup.select('.flex-table__row.searchable')  # Adjust this selector to match the website's structure
    
    fuel_prices = []
    for row in rows:
        try:
            # Extracting the fuel type and price
            fuel_type = row.find('div', {'class': 'cell--lbl'}).text.strip()
            price = row.find('div', {'class': 'cell--val'}).text.strip().replace('kr.', '').strip() + ' kr/l'

            fuel_prices.append({
                'Fuel Type': fuel_type,
                'Price': price
            })
        except (IndexError, TypeError, AttributeError):
            # Skip rows that don't have the expected structure
            continue

    return fuel_prices

def write_to_json(data, output_file_name):
    with open(output_file_name, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

# URL to the OK fuel prices page
ok_url = 'https://www.ok.dk/privat/produkter/ok-kort/benzinpriser'

# Fetch the HTML content from the OK website
html_content = fetch_html(ok_url)

# Parse the HTML content to extract fuel prices
fuel_prices = parse_ok(html_content)

# Output file path for the JSON data
output_file_name = 'stations/ok_prices.json'

# Write the extracted data to a JSON file
write_to_json(fuel_prices, output_file_name)
