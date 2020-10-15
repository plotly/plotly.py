import plotly.graph_objects as go
from _plotly_utils.exceptions import PlotlyKeyError
import pytest


def error_substr(s, r):
    """ remove a part of the error message we don't want to compare """
    return s.replace(r, "")


@pytest.fixture
def some_fig():
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=[], y=[]))
    fig.add_shape(type="rect", x0=1, x1=2, y0=3, y1=4)
    fig.add_shape(type="rect", x0=10, x1=20, y0=30, y1=40)
    fig.add_trace(go.Scatter(x=[1, 2, 3], y=[4, 5, 6]))
    return fig


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
    except ValueError as e:
        assert (
            e.args[0].find(
                """Bad property path:
layout.shapes[1].x2000
                 ^"""
            )
            >= 0
        )


def test_raises_on_bad_ancestor_dot_property(some_fig):

    # Check . property lookup errors but not on the last part of the path
    try:
        x2000 = some_fig["layout.shapa[1].x2000"]
    except ValueError as e:
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
        # get the error without using a path-like key, we compare with this error
        some_fig.data[0].line["colr"] = "blue"
    except ValueError as e_correct:
        # remove "Bad property path:
        e_correct_substr = error_substr(
            e_correct.args[0],
            """
Bad property path:
colr
^""",
        )
    # if the string starts with "Bad property path:" then this test cannot work
    # this way.
    assert len(e_correct_substr) > 0
    try:
        some_fig["data[0].line_colr"] = "blue"
    except ValueError as e:
        e_substr = error_substr(
            e.args[0],
            """
Bad property path:
data[0].line_colr
             ^""",
        )
        assert (
            (
                e.args[0].find(
                    """Bad property path:
data[0].line_colr
             ^"""
                )
                >= 0
            )
            and (e_substr == e_correct_substr)
        )

    try:
        # get the error without using a path-like key
        some_fig.add_trace(go.Scatter(x=[1, 2], y=[3, 4], line=dict(colr="blue")))
    except ValueError as e_correct:
        e_correct_substr = error_substr(
            e_correct.args[0],
            """
Bad property path:
colr
^""",
        )
    # finds bad part when using the path as a keyword argument to a subclass of
    # BasePlotlyType and throws the error for the last good property found in
    # the path
    try:
        some_fig.add_trace(go.Scatter(x=[1, 2], y=[3, 4], line_colr="blue"))
    except ValueError as e:
        e_substr = error_substr(
            e.args[0],
            """
Bad property path:
line_colr
     ^""",
        )
        assert (
            (
                e.args[0].find(
                    """Bad property path:
line_colr
     ^"""
                )
                >= 0
            )
            and (e_substr == e_correct_substr)
        )

    # finds bad part when using the path as a keyword argument to a subclass of
    # BaseFigure and throws the error for the last good property found in
    # the path
    try:
        fig2 = go.Figure(layout=dict(title=dict(txt="two")))
    except ValueError as e_correct:
        e_correct_substr = error_substr(
            e_correct.args[0],
            """
Bad property path:
txt
^""",
        )

    try:
        fig2 = go.Figure(layout_title_txt="two")
    except TypeError as e:
        # when the Figure constructor sees the same ValueError above, a
        # TypeError is raised and adds an error message in front of the same
        # ValueError thrown above
        e_substr = error_substr(
            e.args[0],
            """
Bad property path:
layout_title_txt
             ^""",
        )
        # also remove the invalid Figure property string added by the Figure constructor
        e_substr = error_substr(
            e_substr,
            """invalid Figure property: layout_title_txt
""",
        )
        assert (
            (
                e.args[0].find(
                    """Bad property path:
layout_title_txt
             ^"""
                )
                >= 0
            )
            and (e_substr == e_correct_substr)
        )

    # this is like the above test for subclasses of BasePlotlyType but makes sure it
    # works when the bad part is not the last part in the path
    try:
        some_fig.update_layout(geo=dict(ltaxis=dict(showgrid=True)))
    except ValueError as e_correct:
        e_correct_substr = error_substr(
            e_correct.args[0],
            """
Bad property path:
ltaxis
^""",
        )
    try:
        some_fig.update_layout(geo_ltaxis_showgrid=True)
    except ValueError as e:
        e_substr = error_substr(
            e.args[0],
            """
Bad property path:
geo_ltaxis_showgrid
    ^       """,
        )
        assert (
            (
                e.args[0].find(
                    """Bad property path:
geo_ltaxis_showgrid
    ^"""
                )
                >= 0
            )
            and (e_substr == e_correct_substr)
        )
