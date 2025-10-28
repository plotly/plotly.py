"""Tests for annotated axis-spanning shapes with datetime coordinates.

These tests cover the regression described in GitHub issue #3065:
https://github.com/plotly/plotly.py/issues/3065

"""

from datetime import datetime

import plotly.express as px
import plotly.graph_objects as go


def test_add_vline_with_date_annotation_express():
    """MWE from Github issue https://github.com/plotly/plotly.py/issues/3065"""
    df = px.data.stocks(indexed=True)
    fig = px.line(df)
    fig.add_vline(x="2018-09-24", annotation_text="test")


def test_add_vline_with_date_annotation():
    fig = go.Figure()
    # Provide a couple of traces so axis type is inferred as date from data
    dates = [datetime(2025, 9, 23), datetime(2025, 9, 24), datetime(2025, 9, 25)]
    fig.add_scatter(x=dates, y=[1, 2, 3])
    fig.add_vline(x=dates[1], annotation_text="Test")

    # Ensure one annotation was added and x coordinate preserved
    annotations = getattr(fig.layout, "annotations", [])
    assert len(annotations) == 1
    ann = annotations[0]
    assert ann.x == dates[1]
    assert ann.text == "Test"


def test_add_hline_with_date_annotation():
    fig = go.Figure()
    # Provide a couple of traces so axis type is inferred as date from data
    dates = [datetime(2025, 9, 23), datetime(2025, 9, 24), datetime(2025, 9, 25)]
    fig.add_scatter(y=dates, x=[1, 2, 3])
    fig.add_hline(y=dates[1], annotation_text="Test")

    # Ensure one annotation was added and x coordinate preserved
    annotations = getattr(fig.layout, "annotations", [])
    assert len(annotations) == 1
    ann = annotations[0]
    assert ann.y == dates[1]
    assert ann.text == "Test"
