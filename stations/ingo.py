import requests
import json
from bs4 import BeautifulSoup

def fetch_html(url):
    response = requests.get(url)
    response.raise_for_status()  # Raises an HTTPError for bad responses
    return response.text

def parse_circlek(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    rows = soup.select('.ck-prices-per-product table tbody tr')  # Adjusted selector
    
    fuel_prices = []
    for row in rows:
        cells = row.find_all('td')
        if len(cells) >= 4:  # Ensure there are enough cells in the row
            try:
                fuel_type = cells[1].text.strip().split(':')[1]  # Adjusted to split by ':' and take the second part
                price = cells[2].text.strip().split(':')[1] + ' kr.'  # Adjusted similarly
                date = cells[3].find('time')['datetime'].split('T')[0]  # Extract date
                fuel_prices.append({
                    'Fuel Type': fuel_type,
                    'Price': price,
                    'Last Updated': date
                })
            except (IndexError, TypeError, AttributeError):
                # This handles any unexpected HTML format or missing data
                continue

    return fuel_prices

def write_to_json(data, output_file_name):
    with open(output_file_name, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

# URL to the Ingo fuel prices page (replace with the actual URL if different)
ingo_url = 'https://www.ingo.dk/vores-lave-priser/br%C3%A6ndstofpriser/aktuelle-br%C3%A6ndstofpriser'

# Fetch the HTML content from the Ingo website
html_content = fetch_html(ingo_url)

# Parse the HTML content to extract fuel prices
fuel_prices = parse_circlek(html_content)

# Output file path for the JSON data
output_file_name = 'stations/ingo_prices.json'

# Write the extracted data to a JSON file
write_to_json(fuel_prices, output_file_name)
