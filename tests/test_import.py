import pytest
import plotly.graph_objects as go
from plotly.graph_objects import Scatter


def test_trivial():
    assert Scatter().to_plotly_json() == {"type": "scatter"}


@pytest.fixture
def some_fig():
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=[], y=[]))
    fig.add_shape(type="rect", x0=1, x1=2, y0=3, y1=4)
    fig.add_shape(type="rect", x0=10, x1=20, y0=30, y1=40)
    fig.add_trace(go.Scatter(x=[1, 2, 3], y=[4, 5, 6]))
    return fig


def test_raises_on_bad_index(some_fig):
    with pytest.raises(KeyError):
        some_fig["layout.shapes[2].x0"]
