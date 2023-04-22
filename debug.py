import plotly.express as px
import plotly.graph_objects as go
import numpy as np
from plotly import subplots

test_subplots = True
use_OP = False

df = px.data.iris()
if use_OP:
    fig = px.scatter(df, x="petal_length", y="petal_width")
    fig.add_traces(go.Scatter(y=np.arange(1, 7), mode="lines+markers", yaxis="y2"))

    fig.update_layout(
        yaxis2=dict(
            title="yaxis2 title",
            overlaying="y",
            side="right",
        )
    )
else:
    trace1 = go.Scatter(x=df["petal_length"], y=df["petal_width"], mode="markers")
    trace2 = go.Scatter(
        x=[0, 1, 2, 3, 4, 5], y=np.arange(1, 7), mode="lines+markers", yaxis="y2"
    )
    data = [trace1, trace2]
    layout = go.Layout(
        yaxis=dict(title="yaxis1"),
        yaxis2=dict(title="yaxis2 title", overlaying="y", side="right"),
    )
    fig = go.Figure(data=data, layout=layout)
if test_subplots:
    fig = subplots.make_subplots(rows=1, cols=2, shared_yaxes=False)

fig.add_hline(
    y=2,
    line_dash="dash",
    line_color="Red",  # yref='y2'
    # secondary_y=True
)
fig.show()
