import requests
import json
from bs4 import BeautifulSoup

def fetch_html(url):
    headers = {'User-Agent': 'Mozilla/5.0'}  # Setting a user-agent to mimic a browser
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.text

def parse_f24(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    
    # The actual structure of the F24 page needs to be determined for correct parsing.
    # The provided HTML snippet does not give enough detail about the <tr> and <td> elements.
    # Assuming the structure is similar to the one provided for Circle K, here's an example:
    
    fuel_prices = []
    products = soup.find_all('tr', class_='ng-scope')  # or whatever the correct class/structure is
    for product in products:
        cells = product.find_all('td', class_='ng-scope')  # Modify as per the actual classes/structure
        if len(cells) >= 3:  # Ensure there are enough cells in the row
            try:
                fuel_type = cells[0].text.strip()
                price_excl_vat = cells[1].text.strip() + ' Kr.'
                price_incl_vat = cells[2].text.strip() + ' Kr.'
                fuel_prices.append({
                    'Fuel Type': fuel_type,
                    'Price Excl. VAT': price_excl_vat,
                    'Price Incl. VAT': price_incl_vat
                })
            except (IndexError, TypeError, AttributeError):
                # Handles any unexpected HTML format or missing data
                continue

    return fuel_prices

def write_to_json(data, output_file_name):
    with open(output_file_name, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

# URL to the F24 fuel prices page
f24_url = 'https://www.f24.dk/priser/'

# Fetch the HTML content from the F24 website
html_content = fetch_html(f24_url)

# Parse the HTML content to extract fuel prices
fuel_prices = parse_f24(html_content)

# Output file path for the JSON data
output_file_name = 'stations/f24_prices.json'

# Write the extracted data to a JSON file
write_to_json(fuel_prices, output_file_name)
