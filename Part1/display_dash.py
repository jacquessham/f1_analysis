import dash
import dash_core_components as dcc
import dash_html_components as html
from dashboard_helpers.read_data import fig


# Initiate App
app = dash.Dash(__name__)

# The layout of the dashboard
app.layout = html.Div(children=[
	html.Div([html.H1(children='''Overlaying Speed Traces''')],
             style={'width': '90%', 'margin': 'auto', 'text-align': 'center'}
		),

	html.Div(children='''This is a prototype of a F1 Analysis Prototype'''),
    dcc.Graph(
        id='example-graph', # Name this div
        figure=fig()
    ) # Position 2, children in Div
]) # End Div

if __name__ == '__main__':
    app.run_server(debug=True, host='0.0.0.0', port=8000)
