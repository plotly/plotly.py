import plotly.express as px
import plotly.graph_objects as go
import numpy as np
from plotly.subplots import make_subplots


for k, fun, d, fun2, d2 in [
    (
        "shapes",
        go.Figure.add_shape,
        dict(type="rect", x0=1.5, x1=2.5, y0=3.5, y1=4.5),
        # add a different type to make the check easier (otherwise we might
        # mix up the objects added before and after fun was run)
        go.Figure.add_annotation,
        dict(x=1, y=2, text="A"),
    ),
    (
        "annotations",
        go.Figure.add_annotation,
        dict(x=1, y=2, text="A"),
        go.Figure.add_layout_image,
        dict(x=3, y=4, sizex=2, sizey=3, source="test"),
    ),
    (
        "images",
        go.Figure.add_layout_image,
        dict(x=3, y=4, sizex=2, sizey=3, source="test"),
        go.Figure.add_shape,
        dict(type="rect", x0=1.5, x1=2.5, y0=3.5, y1=4.5),
    ),
]:
    # make a figure where not all the subplots are populated
    fig = make_subplots(2, 2)
    fig.add_trace(go.Scatter(x=[1, 2, 3], y=[5, 1, 2]), row=1, col=1)
    fig.add_trace(go.Scatter(x=[1, 2, 3], y=[2, 1, -7]), row=2, col=2)
    fun2(fig, d2, row=1, col=2)
    # add a thing to all subplots but make sure it only goes on the
    # plots without data or layout objects
    fun(fig, d, row="all", col="all", exclude_empty_subplots="anything_truthy")
    assert len(fig.layout[k]) == 3
    assert fig.layout[k][0]["xref"] == "x" and fig.layout[k][0]["yref"] == "y"
    assert fig.layout[k][1]["xref"] == "x2" and fig.layout[k][1]["yref"] == "y2"
    assert fig.layout[k][2]["xref"] == "x4" and fig.layout[k][2]["yref"] == "y4"
