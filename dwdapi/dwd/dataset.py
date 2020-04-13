import requests
from bs4 import BeautifulSoup
import dwdapi.dwd.stations_description_parsers as parsers
from pathlib import Path
from tqdm import tqdm
from zipfile import ZipFile
import os
import shutil

class DWDDataset():
    """This class specifies a datastructure for a DWD "subproduct" (i.e. hist, rec, now)
    """

    def __init__(self, product, time_period, base_url, stations_description, prefix, suffix):
        self.product = product
        self.time_period = time_period
        self.base_url = base_url
        self.stations_description = stations_description
        self.prefix = prefix
        self.suffix = suffix
        
        # get all the files that exist on the server
        self.__scrape_file_urls()

        # parse the weather stations description
        self.stations = parsers.temp_hourly_parser(self.stations_description)


    def __scrape_file_urls(self):

        req = requests.get(self.base_url)
        soup = BeautifulSoup(req.content, "html.parser")

        anchors = soup.find_all("a")
        links = []

        for a in anchors:
            ref = a.get("href")
            if ref.startswith("stundenwerte_TU_") and ref.endswith(".zip"):
                links.append(ref)
        self.file_urls = links


    def download(self):

        # create folder to place downloaded content in (e.g. dwdapi_temp/temp_hourly/hist)
        download_dir = Path(self.product.temp_dir, self.product.name, self.time_period)
        download_dir.mkdir(parents=True, exist_ok=True)

        print(f"Downloading files to {download_dir}...")
        for url in tqdm(self.file_urls):
            req = requests.get(self.base_url + url)

            filename = Path.joinpath(download_dir, url)
            filename.write_bytes(req.content)

                
            # unzip the file and only keep the extracted content
            with ZipFile(filename, "r") as zippy:
                dirname = Path.joinpath(download_dir, url[:-4])
                if os.path.isdir(dirname):
                    shutil.rmtree(dirname)
                try:

                    dirname.mkdir()
                    zippy.extractall(dirname)
                    os.remove(filename)
                except Exception as e:
                    print(e)


    



    def print(self):
        print(f"    product_name:         {self.product.name}")
        print(f"    time_period:          {self.time_period}")
        print(f"    prefix:               {self.prefix}")
        print(f"    suffix:               {self.suffix}")
        print(f"    base_url:             {self.base_url}")
        print(f"    stations_description: {self.stations_description}")
        #print(f"    file_urls:            {self.file_urls}")
        #print(f"    stations:             {self.stations}")

