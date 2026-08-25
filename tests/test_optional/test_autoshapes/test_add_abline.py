import plotly.graph_objects as go
from plotly.subplots import make_subplots
from itertools import product
import pytest
from .common import _cmp_partial_dict, _check_figure_layout_objects


@pytest.fixture
def single_plot_fixture():
    fig = go.Figure()
    fig.update_xaxes(range=[0, 10])
    fig.add_trace(go.Scatter(x=[], y=[]))
    return fig


@pytest.fixture
def multi_plot_fixture():
    fig = make_subplots(2, 2)
    for r, c in product(range(2), range(2)):
        r += 1
        c += 1
        fig.update_xaxes(row=r, col=c, range=[0, 10])
        fig.add_trace(go.Scatter(x=[], y=[]), row=r, col=c)
    return fig


@pytest.mark.parametrize(
    "test_input,expected",
    [
        (
            (go.Figure.add_abline, dict()),
            [{"type": "line", "x0": 0, "x1": 10, "y0": 0, "y1": 10}],
        ),
        (
            (go.Figure.add_abline, dict(slope=2, intercept=1)),
            [{"type": "line", "x0": 0, "x1": 10, "y0": 1, "y1": 21}],
        ),
        (
            (go.Figure.add_abline, dict(slope=-1, intercept=5)),
            [{"type": "line", "x0": 0, "x1": 10, "y0": 5, "y1": -5}],
        ),
    ],
)
def test_add_abline_single_plot(test_input, expected, single_plot_fixture):
    _check_figure_layout_objects(test_input, expected, single_plot_fixture)


def test_add_abline_default_slope_intercept():
    # slope=1, intercept=0 are the documented defaults
    fig = go.Figure()
    fig.update_xaxes(range=[-3, 3])
    fig.add_abline()
    shape = fig.layout.shapes[0]
    assert (shape.x0, shape.x1) == (-3, 3)
    assert (shape.y0, shape.y1) == (-3, 3)


def test_add_abline_uses_data_range_when_no_explicit_range():
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=[0, 5, 10], y=[1, 2, 3]))
    fig.add_abline(slope=2, intercept=1)
    shape = fig.layout.shapes[0]
    assert (shape.x0, shape.x1) == (0.0, 10.0)
    assert (shape.y0, shape.y1) == (1.0, 21.0)


def test_add_abline_explicit_range_takes_priority_over_data():
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=[0, 5, 10], y=[1, 2, 3]))
    fig.update_xaxes(range=[-5, 5])
    fig.add_abline(slope=1, intercept=0)
    shape = fig.layout.shapes[0]
    assert (shape.x0, shape.x1) == (-5, 5)
    assert (shape.y0, shape.y1) == (-5, 5)


def test_add_abline_falls_back_to_default_range_with_no_data_or_range():
    # No data and no explicit range: falls back to plotly's default (0, 1)
    # x-range rather than raising, matching the documented behavior.
    fig = go.Figure()
    fig.add_abline(slope=3, intercept=2)
    shape = fig.layout.shapes[0]
    assert (shape.x0, shape.x1) == (0, 1)
    assert (shape.y0, shape.y1) == (2, 5)


def test_add_abline_uses_implied_index_range_when_trace_has_no_x():
    # A trace with only y values is drawn against an implied 0..len(y)-1
    # x-index by plotly.js, so add_abline should use that range too.
    fig = go.Figure()
    fig.add_trace(go.Scatter(y=[10, 20, 30, 40]))
    fig.add_abline(slope=1, intercept=0)
    shape = fig.layout.shapes[0]
    assert (shape.x0, shape.x1) == (0, 3)


@pytest.mark.parametrize(
    "test_input,expected",
    [
        (
            (go.Figure.add_abline, dict(slope=1, intercept=0, row=1, col=1)),
            [{"type": "line", "x0": 0, "x1": 10, "xref": "x", "yref": "y"}],
        ),
        (
            (go.Figure.add_abline, dict(slope=1, intercept=0, row=2, col=2)),
            [{"type": "line", "x0": 0, "x1": 10, "xref": "x4", "yref": "y4"}],
        ),
    ],
)
def test_add_abline_subplot_targeting(test_input, expected, multi_plot_fixture):
    _check_figure_layout_objects(test_input, expected, multi_plot_fixture)


def test_add_abline_row_col_all(multi_plot_fixture):
    multi_plot_fixture.add_abline(slope=1, intercept=0, row="all", col="all")
    assert len(multi_plot_fixture.layout.shapes) == 4
    ax_nums = ["", "2", "3", "4"]
    for s, n in zip(multi_plot_fixture.layout.shapes, ax_nums):
        assert _cmp_partial_dict(
            s,
            {
                "type": "line",
                "x0": 0,
                "x1": 10,
                "xref": "x%s" % (n,),
                "yref": "y%s" % (n,),
            },
        )


def test_add_abline_excludes_empty_subplots_by_default():
    fig = make_subplots(rows=1, cols=2)
    fig.update_xaxes(range=[0, 10])
    fig.add_trace(go.Scatter(x=[0, 10], y=[0, 1]), row=1, col=1)
    # col 2 has no trace, so it should be skipped by default
    fig.add_abline(slope=1, intercept=0)
    assert len(fig.layout.shapes) == 1
    assert fig.layout.shapes[0].xref == "x"


def test_add_abline_no_annotation_by_default(multi_plot_fixture):
    multi_plot_fixture.add_abline(slope=1, intercept=0, row="all", col="all")
    assert len(multi_plot_fixture.layout.annotations) == 0
    assert len(multi_plot_fixture.layout.shapes) == 4


def test_add_abline_annotation_single_plot(single_plot_fixture):
    single_plot_fixture.add_abline(slope=1, intercept=0, annotation_text="my line")
    assert len(single_plot_fixture.layout.annotations) == 1
    annotation = single_plot_fixture.layout.annotations[0]
    assert annotation.text == "my line"
    # default annotation_position is "top right": the endpoint with the
    # larger y-value, right-anchored so the text sits to its left
    assert annotation.x == 10
    assert annotation.y == 10
    assert annotation.xanchor == "left"
    assert annotation.yanchor == "top"


def test_add_abline_annotation_position(single_plot_fixture):
    single_plot_fixture.add_abline(
        slope=1,
        intercept=0,
        annotation_text="my line",
        annotation_position="bottom left",
    )
    annotation = single_plot_fixture.layout.annotations[0]
    assert annotation.x == 0
    assert annotation.y == 0
    assert annotation.xanchor == "right"
    assert annotation.yanchor == "bottom"


def test_add_abline_annotation_multi_plot(multi_plot_fixture):
    multi_plot_fixture.add_abline(slope=1, intercept=0, annotation_text="A")
    ax_nums = ["", "2", "3", "4"]
    assert len(multi_plot_fixture.layout.annotations) == 4
    for sh, n in zip(multi_plot_fixture.layout.annotations, ax_nums):
        assert _cmp_partial_dict(
            sh,
            {
                "text": "A",
                "xref": "x%s" % (n,),
                "yref": "y%s" % (n,),
            },
        )


def test_add_abline_returns_figure(single_plot_fixture):
    ret = single_plot_fixture.add_abline(slope=1, intercept=0)
    assert ret is single_plot_fixture
