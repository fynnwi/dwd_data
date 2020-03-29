import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)


app.layout = html.Div([
    dcc.Input(
        id='input_id',
        value='initial value',
        type='text'
    ),
    # the children property of this div is automatically set by the callback upon startup
    html.Div(
        id='div_id'
    ),

    html.Div(
        id='div2_id'
    )
])

# this decorator wraps the update_output function


@app.callback(
    # the two keywords are optional, positional also possible
    [
        Output('div_id', 'children'),
        Output('div2_id', 'children')
    ],
    [
        Input(component_id='input_id', component_property='value')
    ]
)
def update_output_div(input_value):
    return f"You've entered {input_value}.", f"2lele{input_value}"


if __name__ == '__main__':
    app.run_server(debug=True)
