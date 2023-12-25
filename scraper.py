from stations import circlek, f24, ingo, ok, q8

def scrape_station(station_name):
    # Map station names to their respective modules
    station_modules = {
        'circlek': circlek,
        'f24': f24,
        'ingo': ingo,
        'ok': ok,        
        'q8': q8
    }

    # Fetch and return the prices from the respective station module
    if station_name in station_modules:
        return station_modules[station_name]
    else:
        raise ValueError(f"No module found for {station_name}")
