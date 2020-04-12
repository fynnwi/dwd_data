all_products = {
    'temp_hourly': {
        'rec': {
            'base_url': "https://opendata.dwd.de/climate_environment/CDC/observations_germany/climate/hourly/air_temperature/recent/",
            'stations_description': "https://opendata.dwd.de/climate_environment/CDC/observations_germany/climate/hourly/air_temperature/recent/TU_Stundenwerte_Beschreibung_Stationen.txt",
        },
        'hist': {
            'base_url': "https://opendata.dwd.de/climate_environment/CDC/observations_germany/climate/hourly/air_temperature/historical/",
            'stations_description': "https://opendata.dwd.de/climate_environment/CDC/observations_germany/climate/hourly/air_temperature/historical/TU_Stundenwerte_Beschreibung_Stationen.txt",
        },
    }
}





class DWDProduct():

    # inner class
    class DWDDataset():
        def __init__(self, time_period, base_url, stations_description):
            self.time_period = time_period
            self.base_url = base_url
            self.stations_description = stations_description

        def print(self):
            print(f"    time_period:          {self.time_period}")
            print(f"    base_url:             {self.base_url}")
            print(f"    stations_description: {self.stations_description}")


    def __init__(self, name, load_all=None, last=None):
        if name not in all_products.keys():
            raise Exception(f"Product '{name}' not supported!")
        self.name = name
        self.load_all = load_all
        self.last = last

        if self.load_all or self.last > 500:
            print("Warning")

        self.__assign_product_links()




    def __assign_product_links(self):
        self.rec = None
        self.hist = None
        self.now = None
        
        # traverse product dictionary and assign proper values
        keywords = ['rec', 'hist', 'now']
        datasets = {}

        for key, value in all_products[self.name].items():

            try:
                dataset = DWDProduct.DWDDataset(key, value['base_url'], value['stations_description'])
                if key == 'rec': self.rec = dataset
                if key == 'hist': self.hist = dataset
                if key == 'now': self.now = dataset
            except KeyError as e:
                print(f"Error: Key {e} does not exist!")


        print("datasets: ", datasets)


        



    def print(self):
        print(f"PRODUCT:    {self.name}")
        print(f"load_all:   {self.load_all}")
        print(f"last:       {self.last}")

        if self.rec: self.rec.print()
        if self.hist: self.hist.print()
        if self.now: self.now.print()
