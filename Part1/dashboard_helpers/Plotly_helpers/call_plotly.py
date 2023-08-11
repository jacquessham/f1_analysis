import json
import pandas as pd
import plotly
import plotly.graph_objs as go
from plotly.offline import *
from dashboard_helpers.Plotly_helpers.generate_plotly import *


def generate_fig(df):
    with open('/code/dashboard_helpers/Plotly_helpers/arguements.json') as f:
        args = json.load(f)
    fig = generate_plotly_viz(
        df, args['metadata'], args['viz_type'], args['viz_name'])
    return fig