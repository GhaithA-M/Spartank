import requests
import json
from bs4 import BeautifulSoup

def fetch_html(url):
    response = requests.get(url)
    response.raise_for_status()  # Raises an HTTPError for bad responses
    return response.text

def parse_q8(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    price_items = soup.select('.price-item')  # Selects all list items representing products
    
    fuel_prices = []
    for item in price_items:
        try:
            # Extracting the fuel type and price
            fuel_type = item.find('span', {'class': 'display-name'}).text.strip()
            # Replace 'kr./l' with empty string and add ' kr/l' manually
            price = item.find('div', {'class': 'price'}).text.strip().replace('kr./l', '').strip() + ' kr/l'
            
            fuel_prices.append({
                'Fuel Type': fuel_type,
                'Price': price
            })
        except (IndexError, TypeError, AttributeError):
            # Skip items that don't have the expected structure
            continue

    return fuel_prices


def write_to_json(data, output_file_name):
    with open(output_file_name, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

# URL to the Q8 fuel prices page
q8_url = 'https://www.q8.dk/priser/'

# Fetch the HTML content from the Q8 website
html_content = fetch_html(q8_url)

# Parse the HTML content to extract fuel prices
fuel_prices = parse_q8(html_content)

# Output file path for the JSON data
output_file_name = 'stations/q8_prices.json'

# Write the extracted data to a JSON file
write_to_json(fuel_prices, output_file_name)
