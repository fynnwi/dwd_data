import dash
import dash_core_components as dcc
import dash_html_components as html

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)


app.layout = html.Div(
    [
        # Dropdown Menu
        html.Label("Dropdown"),
        dcc.Dropdown(
            options=[
                {'label': "New York City", 'value': "NYC"},
                {'label': "Montreal", 'value': "MTL"},
                {'label': "San Francisco", 'value': "SF"},
            ],
            value='MTL'
        ),

        # Multi-Select Dropdown
        html.Label("Multi-Select Dropdown"),
        dcc.Dropdown(
            options=[
                {'label': "New York City", 'value': 'NYC'},
                {'label': "Montreal", 'value': 'MTL'},
                {'label': "San Francisco", 'value': 'SF'},
            ],
            value=['MTL', 'SF'],
            multi=True
        ),

        # Radio Items
        html.Label("Radio Items"),
        dcc.RadioItems(
            options=[
                {'label': "New York City", 'value': 'NYC'},
                {'label': "Montreal", 'value': 'MTL'},
                {'label': "San Francisco", 'value': 'SF'},
            ],
            value='MTL'
        ),


        # Checkboxes
        html.Label("Checkboxes"),
        dcc.Checklist(
            options=[
                {'label': "New York City", 'value': 'NYC'},
                {'label': "Montreal", 'value': 'MTL'},
                {'label': "San Francisco", 'value': 'SF'},
            ],
            value=['MTL', 'SF']
        ),


        # Text Input
        html.Label("Tetx Input"),
        dcc.Input(
            value='MTL',
            type='text'
        ),


        # Slider
        html.Label("Slider"),
        dcc.Slider(
            min=0,
            max=9,
            marks={
                i: f"Label {i}" if i == 1 else str(i) for i in range(1, 6)
            },
            value=5
        ),
    ],
    
    style={
        'columnCount': 2
    }
)


if __name__ == '__main__':
    app.run_server(debug=True)
