"""
A simple scatter plot
=====================

A scatter plot is created with the plotly library. The figure is interactive,
information are displayed on hover and it is possible to zoom and pan through
the figure.
"""
import plotly.graph_objs as go
import plotly

# Create random data with numpy
import numpy as np

N = 200
random_x = np.random.randn(N)
random_y_0 = np.random.randn(N)
random_y_1 = np.random.randn(N) - 1

# Create traces
trace_0 = go.Scatter(
    x=random_x,
    y=random_y_0,
    mode='markers',
    name='Above',
)
trace_1 = go.Scatter(
    x=random_x,
    y=random_y_1,
    mode='markers',
    name='Below',
)

fig = go.Figure(data=[trace_0, trace_1])
plotly.io.show(fig)

