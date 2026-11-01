"""
Tests for the selection data that reaches an on_selection callback.

Plotly.js keys box and lasso selection data by axis id, so a selection in
the second subplot arrives as {"x2": [...], "y2": [...]}. The widget
resolves that payload against each trace's own axes.
"""

import pytest

import plotly.graph_objs as go
from plotly.subplots import make_subplots

try:
    go.FigureWidget()
except ImportError:
    pytest.skip("FigureWidget is unavailable", allow_module_level=True)


def two_subplots():
    """Return a widget with one trace on x/y and another on x2/y2."""
    fig = make_subplots(rows=1, cols=2)
    fig.add_trace(go.Scatter(x=[1, 2, 3], y=[2, 1, 3]), row=1, col=1)
    fig.add_trace(go.Scatter(x=[10, 11, 20, 21], y=[1, 2, 3, 4]), row=1, col=2)
    return go.FigureWidget(fig)


def select(widget, selector_state, selector_type="box"):
    """
    Fire a selection and return the selector each trace received.

    The selection carries no points, because a box can cover a region of
    the figure that holds no data. That is the case the ranges matter most.
    """
    selectors = []
    for trace in widget.data:
        trace.on_selection(lambda t, p, selector: selectors.append(selector))

    widget._js2py_pointsCallback = {
        "event_type": "plotly_selected",
        "points": {"xs": [], "ys": [], "point_indexes": [], "trace_indexes": []},
        "device_state": None,
        "selector": {"type": selector_type, "selector_state": selector_state},
    }
    return selectors


def test_box_selection_in_the_first_subplot():
    first, second = select(two_subplots(), {"x": [1.1, 2.9], "y": [0.5, 3.5]})

    assert first.xrange == [1.1, 2.9]
    assert first.yrange == [0.5, 3.5]
    # The other subplot was not selected, so it reports nothing.
    assert second.xrange is None
    assert second.yrange is None


def test_box_selection_in_the_second_subplot():
    first, second = select(two_subplots(), {"x2": [12.0, 19.0], "y2": [0.0, 5.0]})

    assert second.xrange == [12.0, 19.0]
    assert second.yrange == [0.0, 5.0]
    assert first.xrange is None
    assert first.yrange is None


def test_box_selection_in_a_figure_without_subplots():
    widget = go.FigureWidget(go.Scatter(x=[1, 2, 3], y=[3, 2, 1]))

    (only,) = select(widget, {"x": [1.0, 2.0], "y": [1.5, 3.0]})

    assert only.xrange == [1.0, 2.0]
    assert only.yrange == [1.5, 3.0]


def test_lasso_selection_in_the_second_subplot():
    first, second = select(two_subplots(), {"x2": [1, 2, 3], "y2": [4, 5, 6]}, "lasso")

    assert second.xs == [1, 2, 3]
    assert second.ys == [4, 5, 6]
    assert first.xs is None
    assert first.ys is None


def test_older_frontend_sends_xrange_and_yrange():
    first, _ = select(two_subplots(), {"xrange": [1.0, 2.0], "yrange": [1.5, 3.0]})

    assert first.xrange == [1.0, 2.0]
    assert first.yrange == [1.5, 3.0]


def test_older_frontend_sends_xs_and_ys():
    first, _ = select(two_subplots(), {"xs": [1, 2, 3], "ys": [4, 5, 6]}, "lasso")

    assert first.xs == [1, 2, 3]
    assert first.ys == [4, 5, 6]
