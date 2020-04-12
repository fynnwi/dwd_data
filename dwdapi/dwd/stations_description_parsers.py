import requests
import pandas as pd


def temp_hourly_parser(url):
    req = requests.get(url)
    text = req.text.splitlines()

    data = []
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
    
    # convert columns to numeric 
    df = df.apply(pd.to_numeric, errors="ignore")
    
    # convert dates into datetime objects
    df[["start_date", "end_date"]] = df[["start_date", "end_date"]].apply(pd.to_datetime, format="%Y%m%d")
    
    return df