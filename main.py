import scraper

def main():
    stations = ['ingo', 'ok', 'f24', 'q8', 'shellservice', 'circlek']
    
    for station in stations:
        try:
            prices = scraper.scrape_station(station)
            print(f"{station.upper()} Prices:")
            for price in prices:
                print(price)
        except ValueError as e:
            print(e)

if __name__ == '__main__':
    main()
