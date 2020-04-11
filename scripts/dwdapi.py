import argparse
import warnings
import os
from pathlib import Path

import requests
from bs4 import BeautifulSoup
from zipfile import ZipFile

import pandas as pd

# arg
parser = argparse.ArgumentParser(
    description="Download weather data from Deutscher Wetterdienst (DWD)",
    epilog="Please note that for data older than 500 days, the complete dataset has to be downloaded which can take a while")

parser.add_argument(
    'product', help='specify product to download from DWD (e.g. "temp_hourly")')

group = parser.add_mutually_exclusive_group(required=True)

group.add_argument('--all', dest='load_all',
                   action='store_true', help='download all available data')

group.add_argument('--last', dest='last', metavar='n',
                   help='download data for the last n days', type=int)

arg_dict = vars(parser.parse_args())
print(arg_dict)


# check if arguments are valid

if arg_dict['load_all'] is None and arg_dict['last'] is None:
    raise Exception("Neither --all nor --last was specified!")

# --last
if arg_dict['last'] is not None:
    if arg_dict['last'] < 1:
        raise Exception("Please enter a negative integer value for --last!")

# check if product exists
supported_products = ['temp_hourly']
prod = arg_dict['product']
if prod not in supported_products:
    raise Exception(f"Product {prod} not supported!")




# TODO implement the rest also
if arg_dict['load_all'] is True or arg_dict['last'] > 500:
    warnings.warn("Loading data older than 500 days is not yet implemented! Only data from last 500 days will be loaded.")






# create all the directories we need
DIR_base = Path("dwdapi_" + prod)
DIR_base.mkdir(parents=True, exist_ok=True)

DIR_temp = Path(DIR_base, "temp")
DIR_temp.mkdir(parents=True, exist_ok=True)


# DWD Open Data server URLS
product_urls = {
    'hourly_temperature_recent': "https://opendata.dwd.de/climate_environment/CDC/observations_germany/climate/hourly/air_temperature/recent/",
    'hourly_temperature_historical': "https://opendata.dwd.de/climate_environment/CDC/observations_germany/climate/hourly/air_temperature/historical/",
}

station_info_files = {
    'hourly_temperature_recent': "TU_Stundenwerte_Beschreibung_Stationen.txt",
    'hourly_temperature_historical': "TU_Stundenwerte_Beschreibung_Stationen.txt",
}




# extract all urls needed for the specified product
product_prefix = "stundenwerte_TU_"
product_suffix = ".zip"

stations_description = list(station_info_files.values())
print(stations_description)



def scrape_product_links(url, prefix, suffix):
    """Get all product file URLs that exist on the server for the specified product
    
    Arguments:
        url {str} -- The root URL pointing to the directory for the specified product
    
    Returns:
        list -- List of URLs pointing to specific product zip file
    """
    req = requests.get(url)
    soup = BeautifulSoup(req.content, 'html.parser')
    anchors = soup.find_all("a")
    links = []
    
    for a in anchors:
        ref = a.get("href")
        if ref.startswith(prefix) and ref.endswith(suffix):
            links.append(url + "/" + ref)
    return links


def download_stations_info(url):
    """extracts information about all the weather stations that were used
    
    Arguments:
        url {str} -- url pointing to the stations description text file
    
    Returns:
        Pandas.DataFrame -- dataframe containing all relevant information
    """

    # request text from server
    req = requests.get(url)
    text = req.text

    text = text.splitlines()
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




def download_product_files(DIR_source, file_urls, DIR_destination, verbose=False):
    """Downloads and extracts all zip files in file_urls and keeps only the extracted content.
    
    Arguments:
        DIR_source {str} -- URL pointing to the product directory on the DWD server
        file_urls {list} -- List of the zip 
        DIR_destination {[type]} -- [description]
    """
    total = len(file_urls)
    if verbose: print(f"Downloading {total} files to {DIR_destination}")
    
    for i, url in enumerate(file_urls, start=1):
        req = requests.get(DIR_source + url)

        filename = Path.joinpath(DIR_destination, url)
        filename.write_bytes(req.content)
            
        # unzip the file and only keep the extracted content
        with ZipFile(filename, "r") as zippy:
            dirname = Path.joinpath(DIR_destination, url[:-4])
            if os.path.isdir(dirname):
                shutil.rmtree(dirname)
            try:
                #os.mkdir(dirname)
                dirname.mkdir()
                zippy.extractall(dirname)
                os.remove(filename)
            except Exception as e:
                print(e)
        if verbose:
            if i % 50 == 0 or i == total:
                print("%d of %d files downloaded" % (i , total))