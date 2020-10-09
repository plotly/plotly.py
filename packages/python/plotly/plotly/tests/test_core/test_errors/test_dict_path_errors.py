import plotly.graph_objects as go
import pytest


@pytest.fixture
def some_fig():
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=[], y=[]))
    fig.add_shape(type="rect", x0=1, x1=2, y0=3, y1=4)
    fig.add_shape(type="rect", x0=10, x1=20, y0=30, y1=40)
    fig.add_trace(go.Scatter(x=[1, 2, 3], y=[4, 5, 6]))
    return fig


# (Unfortunately I couldn't get the match argument of pytest.raises to work
# for multiline regexes so we do the test with assert


def test_raises_on_bad_index(some_fig):
    # Check indexing errors can be detected when path used as key to go.Figure
    try:
        x0 = some_fig["layout.shapes[2].x0"]
    except IndexError as e:
        assert (
            e.args[0].find(
                """Bad property path:
layout.shapes[2].x0
              ^"""
            )
            >= 0
        )


def test_raises_on_bad_dot_property(some_fig):

    # Check . property lookup errors can be detected when path used as key to
    # go.Figure
    try:
        x2000 = some_fig["layout.shapes[1].x2000"]
    except IndexError as e:
        assert (
            e.args[0].find(
                """Bad property path:
layout.shapes[1].x2000
                 ^"""
            )
            >= 0
        )

    # Check . property lookup errors but not on the last part of the path
    try:
        x2000 = some_fig["layout.shapa[1].x2000"]
    except IndexError as e:
        assert (
            e.args[0].find(
                """Bad property path:
layout.shapa[1].x2000
       ^"""
            )
            >= 0
        )


def test_raises_on_bad_indexed_underscore_property(some_fig):

    # finds bad part when using the path as a key to figure and throws the error
    # for the last good property it found in the path
    try:
        some_fig["data[0].line_colr"] = "blue"
    except ValueError as e:
        assert (
            (
                e.args[0].find(
                    """Bad property path:
data[0].line_colr
             ^"""
                )
                >= 0
            )
            and (
                e.args[0].find(
                    """Invalid property specified for object of type plotly.graph_objs.scatter.Line: 'colr'"""
                )
                >= 0
            )
        )

    # finds bad part when using the path as a keyword argument to a subclass of
    # BasePlotlyType and throws the error for the last good property found in
    # the path
    try:
        some_fig.add_trace(go.Scatter(x=[1, 2], y=[3, 4], line_colr="blue"))
    except ValueError as e:
        assert (
            (
                e.args[0].find(
                    """Bad property path:
line_colr
     ^"""
                )
                >= 0
            )
            and (
                e.args[0].find(
                    """Invalid property specified for object of type plotly.graph_objs.layout.shape.Line: 'colr'"""
                )
                >= 0
            )
        )

    # finds bad part when using the path as a keyword argument to a subclass of
    # BaseFigure and throws the error for the last good property found in
    # the path
    try:
        fig2 = go.Figure(layout_title_txt="two")
    except ValueError as e:
        assert (
            (
                e.args[0].find(
                    """Bad property path:
layout_title_txt
             ^"""
                )
                >= 0
            )
            and (
                e.args[0].find(
                    """Invalid property specified for object of type plotly.graph_objs.layout.Title: 'txt'"""
                )
                >= 0
            )
        )

    # this is like the above test for subclasses of BasePlotlyType but makes sure it
    # works when the bad part is not the last part in the path
    try:
        some_fig.update_layout(geo_ltaxis_showgrid=True)
    except ValueError as e:
        assert (
            (
                e.args[0].find(
                    """Bad property path:
geo_ltaxis_showgrid
    ^"""
                )
                >= 0
            )
            and (
                e.args[0].find(
                    """Invalid property specified for object of type plotly.graph_objs.layout.Geo: 'ltaxis'"""
                )
                >= 0
            )
        )
