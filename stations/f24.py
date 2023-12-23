import requests
import json
from bs4 import BeautifulSoup

def fetch_html(url):
    response = requests.get(url)
    response.raise_for_status()  # Raises an HTTPError for bad responses
    print(f"Response status code: {response.status_code}")  # Print the status code
    return response.text

def parse_f24(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    rows = soup.select('tr')  # Adjusted selector to target rows with class 'ng-scope'
    print(f"Number of rows: {len(rows)}")  # Print the number of rows

    fuel_prices = []
    for row in rows:
    print(row) # Print the row
        try:
            # Extracting the fuel type and price
            fuel_type_element = row.find('p', {'ng-switch-when': 'Name'})
            price_element = row.find('p', {'ng-switch-default': ''})

            if fuel_type_element is not None and price_element is not None:
                fuel_type = fuel_type_element.text.strip()
                price = price_element.text.strip().replace('Kr.', '').strip() + ' kr/l'
                print(f"Fuel type: {fuel_type}, Price: {price}")  # Print the fuel type and price

                fuel_prices.append({
                    'Fuel Type': fuel_type,
                    'Price': price
                })
        except (IndexError, TypeError, AttributeError) as e:
            # Print the exception
            print(f"Exception: {e}")
            # Skip rows that don't have the expected structure
            continue

    return fuel_prices

def write_to_json(data, output_file_name):
    with open(output_file_name, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

try:
    # URL to the F24 fuel prices page (replace with the actual URL if different)
    f24_url = 'https://www.f24.dk/priser/'

    # Fetch the HTML content from the F24 website
    html_content = fetch_html(f24_url)

    # Parse the HTML content to extract fuel prices
    fuel_prices = parse_f24(html_content)

    # Output file path for the JSON data
    output_file_name = 'stations/f24_prices.json'

    # Write the extracted data to a JSON file
    write_to_json(fuel_prices, output_file_name)

except Exception as e:
    print(f"Exception: {e}")
