import pytest
import copy
import pickle

from plotly.tools import make_subplots
import plotly.graph_objs as go
import plotly.io as pio


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


@pytest.fixture
def fig_subplots(request):
    fig = make_subplots(3, 2)
    fig.add_scatter(y=[2, 1, 3], row=1, col=1)
    fig.add_scatter(y=[1, 3, 3], row=2, col=2)
    return fig


# Deep copy
# ---------
def test_deepcopy_figure(fig1):
    fig_copied = copy.deepcopy(fig1)

    # Contents should be equal
    assert pio.to_json(fig_copied) == pio.to_json(fig1)

    # Identities should be distinct
    assert fig_copied is not fig1
    assert fig_copied.layout is not fig1.layout
    assert fig_copied.data is not fig1.data


def test_deepcopy_figure_subplots(fig_subplots):
    fig_copied = copy.deepcopy(fig_subplots)

    # Contents should be equal
    assert pio.to_json(fig_copied) == pio.to_json(fig_subplots)

    # Subplot metadata should be equal
    assert fig_subplots._grid_ref == fig_copied._grid_ref
    assert fig_subplots._grid_str == fig_copied._grid_str

    # Identities should be distinct
    assert fig_copied is not fig_subplots
    assert fig_copied.layout is not fig_subplots.layout
    assert fig_copied.data is not fig_subplots.data

    # Should be possible to add new trace to subplot location
    fig_subplots.add_bar(y=[0, 0, 1], row=1, col=2)
    fig_copied.add_bar(y=[0, 0, 1], row=1, col=2)

    # And contents should be still equal
    assert pio.to_json(fig_copied) == pio.to_json(fig_subplots)


def test_deepcopy_layout(fig1):
    copied_layout = copy.deepcopy(fig1.layout)

    # Contents should be equal
    assert copied_layout == fig1.layout

    # Identities should not
    assert copied_layout is not fig1.layout

    # Original layout should still have fig1 as parent
    assert fig1.layout.parent is fig1

    # Copied layout should have no parent
    assert copied_layout.parent is None


# Pickling
# --------
def test_pickle_figure_round_trip(fig1):
    fig_copied = pickle.loads(pickle.dumps(fig1))

    # Contents should be equal
    assert pio.to_json(fig_copied) == pio.to_json(fig1)


def test_pickle_figure_subplots_round_trip(fig_subplots):
    fig_copied = pickle.loads(pickle.dumps(fig_subplots))

    # Contents should be equal
    assert pio.to_json(fig_copied) == pio.to_json(fig_subplots)

    # Should be possible to add new trace to subplot location
    fig_subplots.add_bar(y=[0, 0, 1], row=1, col=2)
    fig_copied.add_bar(y=[0, 0, 1], row=1, col=2)

    # And contents should be still equal
    assert pio.to_json(fig_copied) == pio.to_json(fig_subplots)


def test_pickle_layout(fig1):
    copied_layout = pickle.loads(pickle.dumps(fig1.layout))

    # Contents should be equal
    assert copied_layout == fig1.layout

    # Identities should not
    assert copied_layout is not fig1.layout

    # Original layout should still have fig1 as parent
    assert fig1.layout.parent is fig1

    # Copied layout should have no parent
    assert copied_layout.parent is None
