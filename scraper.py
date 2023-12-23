from stations import ingo, ok, f24, q8, circlek

def scrape_station(station_name):
    # Map station names to their respective modules
    station_modules = {
        'ingo': ingo,
        'ok': ok,
        'f24': f24,
        'q8': q8,
        'circlek': circlek
    }

    # Fetch and return the prices from the respective station module
    if station_name in station_modules:
        return station_modules[station_name]
    else:
        raise ValueError(f"No module found for {station_name}")
