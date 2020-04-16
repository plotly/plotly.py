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
        {"day": False, "time": False, "sex": True, "total_bill": ":.1f"}
    )
    fig = px.scatter(
        df,
        x="tip",
        y="total_bill",
        color="day",
        facet_row="time",
        hover_data=hover_dict,
    )
    for el in ["tip", "total_bill", "sex"]:
        assert el in fig.data[0].hovertemplate
    for el in ["day", "time"]:
        assert el not in fig.data[0].hovertemplate
    assert ":.1f" in fig.data[0].hovertemplate


def test_tuple_hover_data():
    fig = px.scatter(
        x=[1, 2, 3], y=[3, 4, 5], hover_data={"comment": (True, ["a", "b", "c"])}
    )
    assert (
        fig.data[0].hovertemplate
        == "x=%{x}<br>y=%{y}<br>comment=%{customdata[0]}<extra></extra>"
    )
    hover_dicts = [
        {"comment": (":.1f", [1.234, 45.3455, 5666.234])},
        {"comment": (":.1f", np.array([1.234, 45.3455, 5666.234]))},
        {"comment": (":.1f", pd.Series([1.234, 45.3455, 5666.234]))},
    ]
    for hover_dict in hover_dicts:
        fig = px.scatter(x=[1, 2, 3], y=[3, 4, 5], hover_data=hover_dict,)
        assert (
            fig.data[0].hovertemplate
            == "x=%{x}<br>y=%{y}<br>comment=%{customdata[0]:.1f}<extra></extra>"
        )


def test_fail_wrong_column():
    with pytest.raises(ValueError):
        fig = px.scatter(
            {"a": [1, 2], "b": [3, 4], "c": [2, 1]},
            x="a",
            y="b",
            hover_data={"d": True},
        )
    with pytest.raises(ValueError):
        fig = px.scatter(
            {"a": [1, 2], "b": [3, 4], "c": [2, 1]},
            x="a",
            y="b",
            hover_data={"d": ":.1f"},
        )
    with pytest.raises(ValueError):
        fig = px.scatter(
            {"a": [1, 2], "b": [3, 4], "c": [2, 1]},
            x="a",
            y="b",
            hover_data={"d": (True, [3, 4, 5])},
        )
