token = "pk.eyJ1IjoiZnlubndpIiwiYSI6ImNrODk3YmF6MzAzcDczbWs5NXdhaGpyNzYifQ.vHweJb-1hjDeE21tTs7tGQ"

import pandas as pd
us_cities = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/us-cities-top-1k.csv")

import plotly.express as px
data = pd.read_csv("exported_data/stations.csv")


fig = px.scatter_mapbox(data, lat="latitude", lon="longitude", hover_name="station_id", hover_data=['name', 'state'], color_discrete_sequence=['fuchsia'], zoom=3, height=600)

fig.update_layout(mapbox_style='basic', mapbox_accesstoken=token)


fig.update_layout(margin={"r":20,"t":20,"l":20,"b":20})
fig.update_layout(height=600)
fig.show()