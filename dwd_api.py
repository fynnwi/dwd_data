# TODO add argpaser


product_urls = {
    'hourly_temperature_recent': "https://opendata.dwd.de/climate_environment/CDC/observations_germany/climate/hourly/air_temperature/recent/",
    'hourly_temperature_historical': "https://opendata.dwd.de/climate_environment/CDC/observations_germany/climate/hourly/air_temperature/historical/",
}

station_info_files = {
    'hourly_temperature_recent': "TU_Stundenwerte_Beschreibung_Stationen.txt",
    'hourly_temperature_historical': "TU_Stundenwerte_Beschreibung_Stationen.txt",
}



def parse_weather_station_info(text):
    """This function extracts the weather station information from the text file provided by DWD
    
    Arguments:
        text {String} -- the text retrieved vom the DWD Open Data server
    
    Returns:
        df -- pandas dataframe containing weather station information
    """
    data = []
    text = text.splitlines()
    for line in text[2:]:
        e = line.split()
        station_id = e.pop(0)
        start_date = e.pop(0)
        end_date = e.pop(0)
        altitude = e.pop(0)
        latitude = e.pop(0)
        longitude = e.pop(0)
        state = e.pop(-1)
        station_name = " ".join(e)

        row = [station_id, start_date, end_date, altitude, latitude, longitude, station_name, state]
        data.append(row)

    columns = ["station_id", "start_date", "end_date", "altitude", "latitude", "longitude", "name", "state"]
    df = pd.DataFrame(data, columns=columns)
    return df