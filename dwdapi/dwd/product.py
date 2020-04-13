from dwdapi.dwd.dataset import DWDDataset
from pathlib import Path
from tqdm import tqdm
import requests
import os
from zipfile import ZipFile
import shutil


all_products = {
    'temp_hourly': {
        'rec': {
            'base_url': "https://opendata.dwd.de/climate_environment/CDC/observations_germany/climate/hourly/air_temperature/recent/",
            'stations_description': "https://opendata.dwd.de/climate_environment/CDC/observations_germany/climate/hourly/air_temperature/recent/TU_Stundenwerte_Beschreibung_Stationen.txt",
            'prefix': "stundenwerte_TU_",
            'suffix': "_akt.zip",
        },
        'hist': {
            'base_url': "https://opendata.dwd.de/climate_environment/CDC/observations_germany/climate/hourly/air_temperature/historical/",
            'stations_description': "https://opendata.dwd.de/climate_environment/CDC/observations_germany/climate/hourly/air_temperature/historical/TU_Stundenwerte_Beschreibung_Stationen.txt",
            'prefix': "stundenwerte_TU_",
            'suffix': "_hist.zip",
        },
    }
}





class DWDProduct():


    def __init__(self, name, load_all=None, last=None):
        if name not in all_products.keys():
            raise Exception(f"Product '{name}' not supported!")
        self.name = name
        self.load_all = load_all
        self.last = last

        # raise exception if more than 500 days ago is requested (TODO)
        if self.load_all or self.last > 500:
            raise Exception("Currently, only data for the prvious 500 days can be retrieved!")

        
        self.rec = None
        self.hist = None
        self.now = None
        self.__assign_product_links()

        # create a directory for temporary files (for downloads etc.)
        self.temp_dir = Path(Path.cwd(), "dwdapi_temp")
        self.temp_dir.mkdir(exist_ok=True)






    def __assign_product_links(self):
        """This function assigns the correct server URLs to the Product class to be instatiated
        """
        
        
        for key, value in all_products[self.name].items():

            try:
                dataset = DWDDataset(self, key, value['base_url'], value['stations_description'], value['prefix'], value['suffix'])
                if key == 'rec': self.rec = dataset
                if key == 'hist': self.hist = dataset
                if key == 'now': self.now = dataset
            except KeyError as e:
                print(f"Error: Key {e} does not exist!")





    def download(self):
        if self.rec: self.rec.download()
        #if self.hist: self.hist.download()
        if self.now: self.now.download()


    def print(self):
        """Output info about the object to the terminal
        """
        print(f"PRODUCT:    {self.name}")
        print(f"load_all:   {self.load_all}")
        print(f"last:       {self.last}")

        if self.rec: self.rec.print()
        if self.hist: self.hist.print()
        if self.now: self.now.print()
