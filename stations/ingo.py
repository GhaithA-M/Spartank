import requests
from bs4 import BeautifulSoup

def fetch_prices():
    url = 'https://www.ingo.dk/'
    # Your fetching and parsing logic specific to Ingo
    # Return the data in a structured format
    return [{'Fuel Type': 'Benzin 95', 'Price': '13,09 kr.'}]  # Example data
