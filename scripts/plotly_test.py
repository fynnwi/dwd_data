import plotly.graph_objs as go
import pandas as pd
import numpy as np

token = "pk.eyJ1IjoiZnlubndpIiwiYSI6ImNrODk3YmF6MzAzcDczbWs5NXdhaGpyNzYifQ.vHweJb-1hjDeE21tTs7tGQ"

# load data
df = pd.read_csv("exported_data/stations.csv")

lats = df['latitude']
lons = df['longitude']
ids = df['station_id']
names = df['state']
states = df['state']
altitudes = df['altitude']

# create some extra data for testing
temps = np.random.uniform(0, 40, len(altitudes))
temps2 = [x + 5 for x in temps]
temps3 = [x + 10 for x in temps]











# create a figure
fig = go.Figure()

# define my markers
temp_marker = go.scattermapbox.Marker(
    size=12,
    color=temps,
    colorscale="thermal",
    opacity=0.8
)

temp_marker2 = go.scattermapbox.Marker(
    size=15,
    color=temps2,
    colorscale="thermal",
    opacity=0.8
)

temp_marker3 = go.scattermapbox.Marker(
    size=18,
    color=temps3,
    colorscale="thermal",
    opacity=0.8
)


altitude_marker = go.scattermapbox.Marker(
    size=12,
    color=altitudes,
    colorscale="agsunset",
    opacity=0.8
)


# create a trace
trace = go.Scattermapbox(
    lat=lats,
    lon=lons,
    mode='markers',
    marker=temp_marker,
    text=temps
)

fig.add_trace(trace)

# Mapbox
my_mapbox = {
    'accesstoken': token,
    'style': 'basic',
    'zoom': 5,
    'center': {
        'lon': 10.02,
        'lat': 51.13
    }
}

fig.update_layout(
    title="DWD Stations in Germany",
    mapbox=my_mapbox,
    autosize=True)


# Slider
steps = [
    {
        'visible': True,
        'method': "restyle",
        'args': ['marker', temp_marker],
        'label': "1"
    },
    {
        'visible': True,
        'method': "restyle",
        'args': ['marker', temp_marker2],
        'label': "2"
    },
    {
        'visible': True,
        'method': "restyle",
        'args': ['marker', temp_marker3],
        'label': "3"
    }
]


sliders = [{
    'active': 0,
    'steps': steps,
}]

fig.update_layout(sliders=sliders)


# Add dropdown
dropdown = [
    dict(
        buttons=list([
            dict(
                args=["marker", temp_marker],
                label="temperatures",
                method="restyle"
            ),
            dict(
                args=["marker", altitude_marker],
                label="altitudes",
                method="restyle"
            )
        ]),
        direction="left",
        #pad={"r": 10, "t": 20, 'l': 30, 'b': 40},
        showactive=True,
        x=0.9,
        xanchor="left",
        y=1.1,
        yanchor="top"
    ),
]


#fig.update_layout(updatemenus=dropdown)

fig.show()
