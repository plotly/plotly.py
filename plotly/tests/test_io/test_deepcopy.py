import pytest
import copy

import plotly.graph_objs as go

# fixtures
# --------
@pytest.fixture
def fig1(request):
    return go.Figure(data=[{'type': 'scattergl',
                            'marker': {'color': 'green'}},
                           {'type': 'parcoords',
                            'dimensions': [{'values': [1, 2, 3]},
                                           {'values': [3, 2, 1]}],
                            'line': {'color': 'blue'}}],
                     layout={'title': 'Figure title'})


def test_deepcopy(fig1):
    fig1_copied = copy.deepcopy(fig1)
