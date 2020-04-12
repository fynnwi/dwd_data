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
['temp_hourly', 'precip_hourly']





class DWDProduct():

    class DWDDataset():
        def __init__(self, base_url, stations_description):
            self.base_url = base_url
            self.stations_description = stations_description



    def __init__(self, name):
        if name not in all_products.keys():
            raise Exception(f"Product '{name}' not supported!")
        self.name = name
        
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
                datasets[key] = DWDProduct.DWDDataset(value['base_url'], value['stations_description'])
            except KeyError as e:
                print(f"Error: Key {e} does not exist!")


        print()
        print("datasets: ", datasets)


        



    def print(self):
        print(f"Product: {self.name}")
        print(f"rec:     {self.rec}")
        print(f"hist:    {self.hist}")
        print(f"now:     {self.now}")