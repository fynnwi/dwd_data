# Deutscher Wetterdienst Open Data Scraping


This repository containes a Jupyter notebook on how to scrape weather data from the Open Data server of the DWD, as well as a notebook on how to visualize the retrieved data using the Plotly library.

A visualization of some of the results: [https://fynnwi.github.io/](https://fynnwi.github.io/).

A CLI interface is in the making.

## About DWD Open Data
Since 2017, _Deutscher Wetterdienst_ (German Meteorological Service) publishes a lot of its measurements and data publicly available to its [Open Data Server](https://opendata.dwd.de/). An easy access through an API is currently not available, but instead we can browse the server directory tree where tons of data are stored as zip files.

The published data contains weather forecasts from various models, storm warnings, historical climate data and much more. Climate data is published in the directory [/climate_environment/CDC/](https://opendata.dwd.de/climate_environment/CDC/).

The data we are going to have a look at are the **hourly air temperature and humidity measurements at DWD stations in Germany**. They are stored under [this](https://opendata.dwd.de/climate_environment/CDC/observations_germany/climate/hourly/air_temperature/) URL. There exist two folders: `recent` and `historical`. _Recent_ data contains all measurements for the last 500 days until yesterday, and _historical_ data contains all available measurements until the end of the last year (some of which are dating back until the 19th century!). Note that most of the _historical_ data has undergone more steps in the quality control procedure than _recent_ data.

Each zip file on the server corresponds to the measurements of _one_ weather station. Inside a zip file, there is a text file called `produkt_...`, as well as several `Metadaten_...` text/html files. The product file contains the following information:

STATIONS_ID | MESS_DATUM | QN_9 | TT_TU | RF_TU
:---:|:---:|:---:|:---:|:---:
station id | datetime of the measurement | quality level | temperature | relative humidity
... | ... | ... | ... | ...

The meta data files contain information regarding measurement devices and methods, changes in position etc. For the sake of simplicity, I will ignore those information for now.

Additionally, for each product (i.e. hourly temperature recent/historical) the DWD provides the [list of stations](https://opendata.dwd.de/climate_environment/CDC/observations_germany/climate/hourly/air_temperature/recent/TU_Stundenwerte_Beschreibung_Stationen.txt)
involved in creating this product. Through the stations list we can associate temperature measurements with locations in Germany.
The stations list looks like this:

Stations_id | von_datum | bis_datum | Stationshoehe | geoBreite | geoLaenge | Stationsname | Bundesland
:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:
station id | start date | end date | altitude | latitude | longitude | station name | state
... | ... | ... | ... | ... | ... | ... | ...

At the end, we will have a list of 608 weather stations and their locations, as well as the history of the hourly temperature & humidity measurements of these stations.˚
