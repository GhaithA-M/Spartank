import requests
import json

def fetch_json_data(url, payload):
    headers = {'Content-Type': 'application/json'}
    response = requests.post(url, json=payload, headers=headers)
    print("Status Code:", response.status_code)  # Print the status code
    print("Response Headers:", response.headers)  # Print the response headers
    
    try:
        json_data = response.json()
        print("JSON Data:", json_data)  # Print the JSON response
        return json_data
    except json.JSONDecodeError:
        print("Failed to parse JSON. Here's the response text:")
        print(response.text)  # Print the raw response text
        raise  # Re-raise the exception to halt the script

def parse_f24(json_response):
    fuel_prices = []
    for item in json_response["Products"]:  # Adjusted to navigate the JSON structure correctly
        try:
            fuel_type = item['Name']
            price = item['PriceInclVATInclTax'] + " kr/l"  # Append "kr/l" to the price
            fuel_prices.append({
                'Fuel Type': fuel_type,
                'Price': price
            })
        except KeyError:
            continue
    return fuel_prices

def write_to_json(data, output_file_name):
    with open(output_file_name, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

# URL to the F24 fuel prices API
f24_url = 'https://www.f24.dk/-/api/PriceViewProduct/GetPriceViewProducts'

# Define the request payload
payload = {
    "FuelsIdList": [
        {"ProductCode": "22253", "Index": 0},
        {"ProductCode": "22603", "Index": 1},
        {"ProductCode": "24453", "Index": 2},
        {"ProductCode": "24338", "Index": 3}
    ],
    "FromDate": 1700782708,
    "ToDate": 1703374708,
    "TaxIncludeMode": 0,
    "ReportImageUri": None,
    "ColumnInfo": [
        {"Key": "Name", "Title": "Motor-brændstof"},
        {"Key": "PriceExclTaxAndVAT", "Title": "Ekskl. moms og afgifter"},
        {"Key": "PriceInclVATInclTax", "Title": "Inkl. moms og afgifter"}
    ]
}

# Fetch the JSON content from the F24 API
json_response = fetch_json_data(f24_url, payload)

# Parse the JSON content to extract fuel prices
fuel_prices = parse_f24(json_response)

# Output file path for the JSON data
output_file_name = 'stations/f24_prices.json'

# Write the extracted data to a JSON file
write_to_json(fuel_prices, output_file_name)
