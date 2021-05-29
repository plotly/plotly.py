import plotly.graph_objs as go
from plotly.subplots import make_subplots
from plotly.basedatatypes import _indexing_combinations
import plotly.express as px
import pytest
from .common import _cmp_partial_dict, _check_figure_layout_objects


@pytest.fixture
def subplot_fig_fixture():
    fig = px.scatter(
        px.data.tips(), x="total_bill", y="tip", facet_row="smoker", facet_col="sex"
    )
    # explicitly set domains so that we know what they will be
    # these could be anything but we make them plausible
    for ax, dom in zip(
        [("x", ""), ("x", "2"), ("x", "3"), ("x", "4")],
        [(0, 0.4), (0.5, 0.9), (0, 0.4), (0.5, 0.9)],
    ):
        axname = ax[0] + "axis" + ax[1]
        fig["layout"][axname]["domain"] = dom
    for ax, dom in zip(
        [("y", ""), ("y", "2"), ("y", "3"), ("y", "4")],
        [(0, 0.4), (0, 0.4), (0.5, 0.9), (0.5, 0.9)],
    ):
        axname = ax[0] + "axis" + ax[1]
        fig["layout"][axname]["domain"] = dom
    return fig


@pytest.fixture
def subplot_empty_traces_fig_fixture():
    fig = px.scatter(
        px.data.tips(), x="total_bill", y="tip", facet_row="day", facet_col="time"
    )
    # explicitly set domains so that we know what they will be
    # these could be anything but we make them plausible
    for ax, dom in zip(
        [("x", "")] + [("x", str(n)) for n in range(2, 9)],
        [((n % 2) * 0.5, (n % 2) * 0.5 + 0.4) for n in range(8)],
    ):
        axname = ax[0] + "axis" + ax[1]
        fig["layout"][axname]["domain"] = dom
    for ax, dom in zip(
        [("y", "")] + [("y", str(n)) for n in range(2, 9)],
        [((n // 2) * 0.25, (n // 2) * 0.25 + 0.2) for n in range(8)],
    ):
        axname = ax[0] + "axis" + ax[1]
        fig["layout"][axname]["domain"] = dom
    return fig


@pytest.fixture
def non_subplot_fig_fixture():
    fig = go.Figure(go.Scatter(x=[1, 2, 3], y=[4, 3, 2]))
    return fig


# Fixture is here for testing custom-sized subplots
@pytest.fixture
def custom_sized_subplots():
    fig = make_subplots(
        rows=5,
        cols=2,
        specs=[
            [{}, {"rowspan": 2}],
            [{}, None],
            [{"rowspan": 2, "colspan": 2}, None],
            [None, None],
            [{}, {}],
        ],
        print_grid=True,
    )

    fig.add_trace(go.Scatter(x=[1, 2], y=[1, 2], name="(1,1)"), row=1, col=1)
    fig.add_trace(go.Scatter(x=[1, 2], y=[1, 2], name="(1,2)"), row=1, col=2)
    fig.add_trace(go.Scatter(x=[1, 2], y=[1, 2], name="(2,1)"), row=2, col=1)
    fig.add_trace(go.Scatter(x=[1, 2], y=[1, 2], name="(3,1)"), row=3, col=1)
    fig.add_trace(go.Scatter(x=[1, 2], y=[1, 2], name="(5,1)"), row=5, col=1)
    fig.add_trace(go.Scatter(x=[1, 2], y=[1, 2], name="(5,2)"), row=5, col=2)
    return fig


# stuff to test:
# add_vline, hline etc. add the intended shape
#   - then WLOG maybe we can just test 1 of them, e.g., add_vline?
# test that the addressing works correctly? this is already tested for in add_shape...
# make sure all the methods work for subplots and single plot
# test edge-cases of _make_paper_spanning_shape: bad direction, bad shape (e.g., a path)


@pytest.mark.parametrize(
    "test_input,expected",
    # test_input: (function,kwargs)
    # expected: list of dictionaries with key:value pairs we expect in the added shapes
    [
        (
            (go.Figure.add_vline, dict(x=20, row=1, col=1)),
            [
                {
                    "type": "line",
                    "x0": 20,
                    "x1": 20,
                    "xref": "x",
                    "y0": 0,
                    "y1": 1,
                    "yref": "y domain",
                }
            ],
        ),
        (
            (go.Figure.add_vline, dict(x=20, row=2, col=2)),
            [
                {
                    "type": "line",
                    "x0": 20,
                    "x1": 20,
                    "xref": "x4",
                    "y0": 0,
                    "y1": 1,
                    "yref": "y4 domain",
                }
            ],
        ),
        (
            (go.Figure.add_hline, dict(y=6, row=1, col=1)),
            [
                {
                    "type": "line",
                    "x0": 0,
                    "x1": 1,
                    "xref": "x domain",
                    "y0": 6,
                    "y1": 6,
                    "yref": "y",
                }
            ],
        ),
        (
            (go.Figure.add_hline, dict(y=6, row=2, col=2)),
            [
                {
                    "type": "line",
                    "x0": 0,
                    "x1": 1,
                    "xref": "x4 domain",
                    "y0": 6,
                    "y1": 6,
                    "yref": "y4",
                }
            ],
        ),
        (
            (go.Figure.add_vrect, dict(x0=20, x1=30, row=1, col=1)),
            [
                {
                    "type": "rect",
                    "x0": 20,
                    "x1": 30,
                    "xref": "x",
                    "y0": 0,
                    "y1": 1,
                    "yref": "y domain",
                }
            ],
        ),
        (
            (go.Figure.add_vrect, dict(x0=20, x1=30, row=2, col=2)),
            [
                {
                    "type": "rect",
                    "x0": 20,
                    "x1": 30,
                    "xref": "x4",
                    "y0": 0,
                    "y1": 1,
                    "yref": "y4 domain",
                }
            ],
        ),
        (
            (go.Figure.add_hrect, dict(y0=6, y1=8, row=1, col=1)),
            [
                {
                    "type": "rect",
                    "x0": 0,
                    "x1": 1,
                    "xref": "x domain",
                    "y0": 6,
                    "y1": 8,
                    "yref": "y",
                }
            ],
        ),
        (
            (go.Figure.add_hrect, dict(y0=6, y1=8, row=2, col=2)),
            [
                {
                    "type": "rect",
                    "x0": 0,
                    "x1": 1,
                    "xref": "x4 domain",
                    "y0": 6,
                    "y1": 8,
                    "yref": "y4",
                }
            ],
        ),
        (
            (go.Figure.add_vline, dict(x=20, row=2, col="all")),
            [
                {
                    "type": "line",
                    "x0": 20,
                    "x1": 20,
                    "xref": "x3",
                    "y0": 0,
                    "y1": 1,
                    "yref": "y3 domain",
                },
                {
                    "type": "line",
                    "x0": 20,
                    "x1": 20,
                    "xref": "x4",
                    "y0": 0,
                    "y1": 1,
                    "yref": "y4 domain",
                },
            ],
        ),
        (
            (go.Figure.add_vline, dict(x=20, row="all", col=2)),
            [
                {
                    "type": "line",
                    "x0": 20,
                    "x1": 20,
                    "xref": "x2",
                    "y0": 0,
                    "y1": 1,
                    "yref": "y2 domain",
                },
                {
                    "type": "line",
                    "x0": 20,
                    "x1": 20,
                    "xref": "x4",
                    "y0": 0,
                    "y1": 1,
                    "yref": "y4 domain",
                },
            ],
        ),
    ],
)
def test_add_span_shape(test_input, expected, subplot_fig_fixture):
    _check_figure_layout_objects(test_input, expected, subplot_fig_fixture)


@pytest.mark.parametrize(
    "test_input,expected",
    # test_input: (function,kwargs)
    # expected: list of dictionaries with key:value pairs we expect in the added shapes
    [
        (
            (go.Figure.add_vline, dict(x=20, row=[3, 4], col="all")),
            [
                {
                    "type": "line",
                    "x0": 20,
                    "x1": 20,
                    "xref": "x5",
                    "y0": 0,
                    "y1": 1,
                    "yref": "y5 domain",
                },
                {
                    "type": "line",
                    "x0": 20,
                    "x1": 20,
                    "xref": "x7",
                    "y0": 0,
                    "y1": 1,
                    "yref": "y7 domain",
                },
            ],
        ),
        (
            (
                go.Figure.add_vline,
                dict(x=20, row="all", col=2, exclude_empty_subplots=False),
            ),
            [
                {
                    "type": "line",
                    "x0": 20,
                    "x1": 20,
                    "xref": "x2",
                    "y0": 0,
                    "y1": 1,
                    "yref": "y2 domain",
                },
                {
                    "type": "line",
                    "x0": 20,
                    "x1": 20,
                    "xref": "x4",
                    "y0": 0,
                    "y1": 1,
                    "yref": "y4 domain",
                },
                {
                    "type": "line",
                    "x0": 20,
                    "x1": 20,
                    "xref": "x6",
                    "y0": 0,
                    "y1": 1,
                    "yref": "y6 domain",
                },
                {
                    "type": "line",
                    "x0": 20,
                    "x1": 20,
                    "xref": "x8",
                    "y0": 0,
                    "y1": 1,
                    "yref": "y8 domain",
                },
            ],
        ),
    ],
)
def test_add_span_shape_no_empty_plot(
    test_input, expected, subplot_empty_traces_fig_fixture
):
    _check_figure_layout_objects(test_input, expected, subplot_empty_traces_fig_fixture)


@pytest.mark.parametrize(
    "test_input,expected",
    # test_input: (function,kwargs)
    # expected: list of dictionaries with key:value pairs we expect in the added shapes
    [
        (
            (go.Figure.add_hline, dict(y=6)),
            [
                {
                    "type": "line",
                    "x0": 0,
                    "x1": 1,
                    "xref": "x domain",
                    "y0": 6,
                    "y1": 6,
                    "yref": "y",
                }
            ],
        ),
        (
            (go.Figure.add_vline, dict(x=6)),
            [
                {
                    "type": "line",
                    "y0": 0,
                    "y1": 1,
                    "xref": "x",
                    "x0": 6,
                    "x1": 6,
                    "yref": "y domain",
                }
            ],
        ),
    ],
)
def test_non_subplot_add_span_shape(test_input, expected, non_subplot_fig_fixture):
    _check_figure_layout_objects(test_input, expected, non_subplot_fig_fixture)


@pytest.mark.parametrize(
    "test_input",
    [
        (go.Figure.add_hline, dict(y=10, row=4, col=5)),
        # valid row, invalid column
        (go.Figure.add_hline, dict(y=10, row=1, col=5)),
    ],
)
def test_invalid_subplot_address(test_input, subplot_fig_fixture):
    f, kwargs = test_input
    with pytest.raises(IndexError):
        f(subplot_fig_fixture, **kwargs)


def _check_figure_shapes_custom_sized(test_input, expected, fig):
    # look up domains in fig
    corrects = []
    for d, ax in expected:
        dom = [0, 1]
        if ax[: len("xaxis")] == "xaxis":
            d["x0"], d["x1"] = dom
        elif ax[: len("yaxis")] == "yaxis":
            d["y0"], d["y1"] = dom
        else:
            raise ValueError("bad axis")
        corrects.append(d)
    f, kwargs = test_input
    f(fig, **kwargs)
    if len(fig.layout.shapes) == 0:
        assert False
    if len(fig.layout.shapes) != len(corrects):
        assert False
    ret = True
    for s, d in zip(fig.layout.shapes, corrects):
        ret &= _cmp_partial_dict(s, d)
    assert ret


@pytest.mark.parametrize(
    "test_input,expected",
    # test_input: (function,kwargs)
    # expected: list of dictionaries with key:value pairs we expect in the added shapes
    [
        (
            (go.Figure.add_vline, dict(x=1.5, row="all", col=2)),
            [
                (
                    {
                        "type": "line",
                        "x0": 1.5,
                        "x1": 1.5,
                        "xref": "x2",
                        "yref": "y2 domain",
                    },
                    "yaxis2",
                ),
                (
                    {
                        "type": "line",
                        "x0": 1.5,
                        "x1": 1.5,
                        "xref": "x6",
                        "yref": "y6 domain",
                    },
                    "yaxis6",
                ),
            ],
        ),
        (
            (go.Figure.add_hline, dict(y=1.5, row=5, col="all")),
            [
                (
                    {
                        "type": "line",
                        "yref": "y5",
                        "y0": 1.5,
                        "y1": 1.5,
                        "xref": "x5 domain",
                    },
                    "xaxis5",
                ),
                (
                    {
                        "type": "line",
                        "yref": "y6",
                        "y0": 1.5,
                        "y1": 1.5,
                        "xref": "x6 domain",
                    },
                    "xaxis6",
                ),
            ],
        ),
    ],
)
def test_custom_sized_subplots(test_input, expected, custom_sized_subplots):
    _check_figure_shapes_custom_sized(test_input, expected, custom_sized_subplots)
