import plotly.graph_objs as go
from plotly.subplots import make_subplots
from plotly.basedatatypes import _indexing_combinations, _unzip_pairs
import plotly.express as px
import pytest


@pytest.fixture
def subplot_fig_fixture():
    fig = px.scatter(
        px.data.tips(), x="total_bill", y="tip", facet_row="smoker", facet_col="sex"
    )
    # explicitly set domains so that we know what they will be
    for ax in ["x", "y"]:
        for n in range(1, 5):
            axname = ax + "axis" + str(n) if n != 1 else ax + "axis"
            start = ((n - 1) // 2) * 0.5
            stop = start + 0.4
            fig["layout"][axname]["domain"] = [start, stop]
    return fig


@pytest.fixture
def subplot_empty_traces_fig_fixture():
    fig = px.scatter(
        px.data.tips(), x="total_bill", y="tip", facet_row="day", facet_col="time"
    )


@pytest.fixture
def non_subplot_fig_fixture():
    fig = go.Figure(go.Scatter(x=[1, 2, 3], y=[4, 3, 2]))
    return fig


# stuff to test:
# add_vline, hline etc. add the intended shape
#   - then WLOG maybe we can just test 1 of them, e.g., add_vline?
# test that the addressing works correctly? this is already tested for in add_shape...
# make sure all the methods work for subplots and single plot
# test edge-cases of _make_paper_spanning_shape: bad direction, bad shape (e.g., a path)


def _cmp_partial_dict(a, b):
    ret = True
    for k in b.keys():
        try:
            v = a[k]
            ret &= v == b[k]
        except KeyError:
            return False
    return ret


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
                    "y1": 0.4,
                    "yref": "paper",
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
                    "y0": 0.5,
                    "y1": 0.9,
                    "yref": "paper",
                }
            ],
        ),
        (
            (go.Figure.add_hline, dict(y=6, row=1, col=1)),
            [
                {
                    "type": "line",
                    "x0": 0,
                    "x1": 0.4,
                    "xref": "paper",
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
                    "x0": 0.5,
                    "x1": 0.9,
                    "xref": "paper",
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
                    "y1": 0.4,
                    "yref": "paper",
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
                    "y0": 0.5,
                    "y1": 0.9,
                    "yref": "paper",
                }
            ],
        ),
        (
            (go.Figure.add_hrect, dict(y0=6, y1=8, row=1, col=1)),
            [
                {
                    "type": "rect",
                    "x0": 0,
                    "x1": 0.4,
                    "xref": "paper",
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
                    "x0": 0.5,
                    "x1": 0.9,
                    "xref": "paper",
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
                    "y0": 0.5,
                    "y1": 0.9,
                    "yref": "paper",
                },
                {
                    "type": "line",
                    "x0": 20,
                    "x1": 20,
                    "xref": "x4",
                    "y0": 0.5,
                    "y1": 0.9,
                    "yref": "paper",
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
                    "y1": 0.4,
                    "yref": "paper",
                },
                {
                    "type": "line",
                    "x0": 20,
                    "x1": 20,
                    "xref": "x4",
                    "y0": 0.5,
                    "y1": 0.9,
                    "yref": "paper",
                },
            ],
        ),
    ],
)
def test_add_span_shape(test_input, expected, subplot_fig_fixture):
    f, kwargs = test_input
    f(subplot_fig_fixture, **kwargs)
    ret = True
    for s, d in zip(subplot_fig_fixture.layout.shapes, expected):
        ret &= _cmp_partial_dict(s, d)
    assert ret
