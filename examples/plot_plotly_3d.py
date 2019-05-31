"""
Topographical 3D Surface Plot
=============================

A 3D surface plot showing the topograph of Mount Bruno (Quebec). Try to
rotate (left button and drag) and scale (scroll) this animated 3D plot.
"""
import plotly
import plotly.graph_objs as go

import pandas as pd

# Read data from a csv
z_data = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/api_docs/mt_bruno_elevation.csv')

data = [go.Surface(z=z_data)
       ]
layout = go.Layout(
    title='Mt Bruno Elevation',
    autosize=False,
    width=600,
    height=600,
    margin=dict(
        l=65,
        r=50,
        b=65,
        t=90
    )
)
fig = go.Figure(data=data, layout=layout)
plotly.io.show(fig)
