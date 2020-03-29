import dash
import dash_core_components as dcc
import dash_html_components as html

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

city1 = "San Francisco"
city2 = "Montreal"

colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}

# Layout
app.layout = html.Div(
    style={
        'backgroundColor': colors['background']
    },
    children=[
        html.H1(
            children="Hello Dash",
            style={
                'textAlign': 'center',
                'color': colors['text']
            }),

        html.Div(
            children="Dash: A web app framework for Python.",
            style={
                'textAlign': 'center',
                'color': colors['text']
            }),

        dcc.Graph(
            id="example graph",
            figure={
                'data': [
                    dict(x=[1, 2, 3], y=[4, 1, 2],
                         type='bar', name=f"{city1}"),
                    dict(x=[1, 2, 3], y=[2, 4, 5],
                         type='bar', name=f"{city2}"),
                ],
                'layout': {
                    'plot_bgcolor': colors['background'],
                    'paper_bgcolor': colors['background'],
                    'font': {
                        'color': colors['text']
                    }
                }
            }
        )
    ])

if __name__ == '__main__':
    app.run_server(debug=True)
