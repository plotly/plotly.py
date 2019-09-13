import plotly.express as px
import numpy as np
import pandas as pd
import pytest


def test_numpy():
    fig = px.scatter(x=[1, 2, 3], y=[2, 3, 4], color=[1, 3, 9])


def test_numpy_labels():
    fig = px.scatter(
        x=[1, 2, 3], y=[2, 3, 4], labels={"x": "time"}
    )  # other labels will be kw arguments
    assert fig.data[0]["hovertemplate"] == "time=%{x}<br>y=%{y}"


def test_with_index():
    tips = px.data.tips()
    fig = px.scatter(tips, x="index", y="total_bill")
    fig = px.scatter(tips, x="index", y=tips.total_bill)
    assert fig.data[0]["hovertemplate"] == "index=%{x}<br>total_bill=%{y}"
    # I was not expecting this to work but it does...
    fig = px.scatter(tips, x="index", y=10 * tips.total_bill)
    assert fig.data[0]["hovertemplate"] == "index=%{x}<br>total_bill=%{y}"


def test_mixed_case():
    df = pd.DataFrame(dict(time=[1, 2, 3], temperature=[20, 30, 25]))
    fig = px.scatter(df, x="time", y="temperature", color=[1, 3, 9])


def test_wrong_column_name():
    with pytest.raises(ValueError):
        fig = px.scatter(px.data.tips(), x="bla", y="wrong")
