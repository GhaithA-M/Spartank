import requests
import json
from bs4 import BeautifulSoup

# Function to fetch HTML content from F24
def fetch_html(url):
    response = requests.get(url)
    response.raise_for_status()
    return response.text

# Function to parse the HTML and extract fuel prices for F24
def parse_f24(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    # Check if the priceDevelopment-table exists in the content
    price_table_container = soup.find('div', class_='priceDevelopment-table')
    if not price_table_container:
        return []  # Return an empty list if the container is not found
    
    price_table = price_table_container.find('table')
    fuel_prices = []

    if price_table:
        rows = price_table.find('tbody').find_all('tr', class_='ng-scope')
        for row in rows:
            cols = row.find_all('td', class_='ng-scope')
            if cols and len(cols) == 3:
                fuel_name_info = cols[0].find('p', class_='ng-binding')
                fuel_name = fuel_name_info.text.strip() if fuel_name_info else 'N/A'

                price_info = cols[2].find('p', class_='ng-binding')
                price = price_info.text.strip() if price_info else 'N/A'

                # Add date extraction logic here if the date is available in the HTML

                fuel_prices.append({
                    'Fuel Type': fuel_name,
                    'Price': price
                    # 'Last Updated': last_updated  # Add this if you have the date information
                })

    return fuel_prices


def write_to_json(data, output_file_name):
    with open(output_file_name, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

# F24 URL to fetch prices from
f24_url = 'https://www.f24.dk/priser/'

# Fetch the HTML content
html_content = fetch_html(f24_url)

# Parse the HTML content
fuel_prices = parse_f24(html_content)

# Write the extracted data to a JSON file
output_file_name = 'stations/f24_prices.json'
write_to_json(fuel_prices, output_file_name)
