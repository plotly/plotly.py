import plotly.graph_objs as go
from plotly.subplots import make_subplots
from plotly.basedatatypes import _indexing_combinations, _unzip_pairs
import pytest

NROWS = 4
NCOLS = 5


@pytest.fixture
def subplot_fig_fixture():
    fig = make_subplots(NROWS, NCOLS)
    return fig


@pytest.fixture
def non_subplot_fig_fixture():
    fig = go.Figure(go.Scatter(x=[1, 2, 3], y=[4, 3, 2]))
    return fig


# stuff to test:
# add_vline, hline etc. add the intended shape
#   - then WLOG maybe we can just test 1 of them, e.g., add_vline?
# test that the addressing works correctly? this is already tested for add_shape...
# make sure all the methods work for subplots and single plot
# test edge-cases of _make_paper_spanning_shape: bad direction, bad shape (e.g., a path)
