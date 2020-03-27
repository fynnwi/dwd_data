token = "pk.eyJ1IjoiZnlubndpIiwiYSI6ImNrODk3YmF6MzAzcDczbWs5NXdhaGpyNzYifQ.vHweJb-1hjDeE21tTs7tGQ"

import pandas as pd
us_cities = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/us-cities-top-1k.csv")

import plotly.express as px
data = pd.read_csv("exported_data/stations.csv")
data['color'] = '#ff7f0e'


fig = px.scatter_mapbox(data, lat="latitude", lon="longitude", hover_name="station_id", hover_data=['name', 'state'], zoom=5,)

fig.update_layout(mapbox_style='basic', mapbox_accesstoken=token)
fig.update_layout(margin=dict(t=25, b=10, l=30, r=30))
fig.update_layout(height=700)


# fig.update_traces(marker=dict(size=12, color=data['altitude'], colorscale='Cividis'))




# Add dropdown
fig.update_layout(
    updatemenus=[
        dict(
            buttons=list([
                dict(
                    args=["color", 0],
                    label="states",
                    method="restyle"
                ),
                dict(
                    args=["color", data['state']],
                    label="altitude",
                    method="restyle"
                )
            ]),
            direction="down",
            pad={"r": 10, "t": 0},
            showactive=True,
            x=0.1,
            xanchor="left",
            y=1.1,
            yanchor="top"
        ),
    ]
)


# Add annotation
fig.update_layout(
    annotations=[
        dict(text="Color by: ", showarrow=False,
        x=0, y=1.085, yref="paper", align="left")
    ]
)





fig.show()