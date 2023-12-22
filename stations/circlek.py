import requests
import json
from bs4 import BeautifulSoup

def fetch_html(url):
    response = requests.get(url)
    response.raise_for_status()  # Raises an HTTPError if the HTTP request returned an unsuccessful status code
    return response.text

def parse_circlek(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    prices_table = soup.find('table', class_='uk-table uk-table-striped uk-table-responsive')
    fuel_prices = []

    if prices_table:
        rows = prices_table.find_all('tr')[1:]  # Skip header row
        for row in rows:
            cols = row.find_all('td')
            product_name = cols[1].get_text(strip=True)
            price = cols[2].get_text(strip=True).replace(' kr.', '')  # Remove ' kr.' from the price
            date = cols[3].find('time').get('datetime', '').split('T')[0]  # Extract date only
            fuel_prices.append({
                'product_name': product_name,
                'price': price,
                'date': date
            })

    return fuel_prices

def write_to_json(data, output_file_path):
    with open(output_file_path, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

# Example usage:
circlek_url = 'https://www.circlek.dk/priser'  # Replace with the correct URL
output_file_path = 'stations/circlek_prices.json'  # Replace with the desired output path

# Fetch HTML content
html_content = fetch_html(circlek_url)

# Parse the HTML content
circlek_prices = parse_circlek(html_content)

# Write the parsed data to a JSON file
write_to_json(circlek_prices, output_file_path)
