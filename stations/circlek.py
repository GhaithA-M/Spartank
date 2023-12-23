import requests
import json
from bs4 import BeautifulSoup

def fetch_html(url):
    response = requests.get(url)
    response.raise_for_status()  # Raises an HTTPError for bad responses
    return response.text

def parse_circlek(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    rows = soup.find_all('tr')
    
    fuel_prices = []
    for row in rows:
        cells = row.find_all('td')
        if len(cells) >= 6:  # Ensure there are enough cells in the row
            try:
                # Remove 'Beskrivelse:' from the fuel type and remove the dot
                fuel_type = cells[1].text.strip().replace('Beskrivelse: ', '').replace('.', '')
                # Remove 'Pris inkl. moms:' from the price
                price = cells[2].text.strip().replace('Pris inkl. moms: ', '') + ' kr/l'
                date = cells[3].find('time')['datetime'].split('T')[0]  # Extract date
                
                # Exclude 'Fyringsolie' and 'El Lynlader' entries
                if 'Fyringsolie' not in fuel_type and 'El Lynlader' not in fuel_type:
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

# URL to the Circle K fuel prices page
circlek_url = 'https://www.circlek.dk/priser'

# Fetch the HTML content from the Circle K website
html_content = fetch_html(circlek_url)

# Parse the HTML content to extract fuel prices
fuel_prices = parse_circlek(html_content)

# Output file path for the JSON data
output_file_name = 'stations/circlek_prices.json'

# Write the extracted data to a JSON file
write_to_json(fuel_prices, output_file_name)
