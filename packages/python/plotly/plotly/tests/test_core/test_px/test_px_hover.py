import plotly.express as px
import numpy as np
import pandas as pd
import pytest
import plotly.graph_objects as go
from collections import OrderedDict  # an OrderedDict is needed for Python 2


def test_skip_hover():
    df = px.data.iris()
    fig = px.scatter(
        df,
        x="petal_length",
        y="petal_width",
        size="species_id",
        hover_data={"petal_length": None, "petal_width": None},
    )
    assert fig.data[0].hovertemplate == "species_id=%{marker.size}<extra></extra>"


def test_composite_hover():
    df = px.data.tips()
    hover_dict = OrderedDict(
            {"day": False, "sex": True, "time": False, "total_bill": ":.1f"}
    )
    fig = px.scatter(
        df,
        x="tip",
        y="total_bill",
        color="day",
        facet_row="time",
        hover_data=hover_dict,
    )
    assert (
        fig.data[0].hovertemplate
        == "tip=%{x}<br>total_bill=%{customdata[1]:.1f}<br>sex=%{customdata[0]}<extra></extra>"
    )
