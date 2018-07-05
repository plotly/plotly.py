from __future__ import absolute_import
from unittest import skip

from plotly.graph_objs import Data, Figure, Layout, Line, Scatter, scatter, XAxis
from plotly.tests.utils import strip_dict_params


def test_update_dict():
    title = 'this'
    fig = Figure()
    fig.update(layout=Layout(title=title))
    assert fig == Figure(layout=Layout(title=title))
    fig['layout'].update(xaxis=XAxis())
    assert fig == Figure(layout=Layout(title=title, xaxis=XAxis()))


def test_update_list():
    trace1 = Scatter(x=[1, 2, 3], y=[2, 1, 2])
    trace2 = Scatter(x=[1, 2, 3], y=[3, 2, 1])
    fig = Figure([trace1, trace2])
    update = dict(x=[2, 3, 4], y=[1, 2, 3])
    fig.data[0].update(update)
    fig.data[1].update(update)

    d1, d2 = strip_dict_params(fig.data[0], Scatter(x=[2, 3, 4], y=[1, 2, 3]))
    assert d1 == d2
    d1, d2 = strip_dict_params(fig.data[1], Scatter(x=[2, 3, 4], y=[1, 2, 3]))
    assert d1 == d2


def test_update_dict_empty():
    trace1 = Scatter(x=[1, 2, 3], y=[2, 1, 2])
    trace2 = Scatter(x=[1, 2, 3], y=[3, 2, 1])
    fig = Figure([trace1, trace2])
    fig.update({})
    d1, d2 = strip_dict_params(fig.data[0], Scatter(x=[1, 2, 3], y=[2, 1, 2]))
    assert d1 == d2
    d1, d2 = strip_dict_params(fig.data[1], Scatter(x=[1, 2, 3], y=[3, 2, 1]))
    assert d1 == d2


def test_update_list_empty():
    trace1 = Scatter(x=[1, 2, 3], y=[2, 1, 2])
    trace2 = Scatter(x=[1, 2, 3], y=[3, 2, 1])
    fig = Figure([trace1, trace2])
    fig.update([])
    d1, d2 = strip_dict_params(fig.data[0], Scatter(x=[1, 2, 3], y=[2, 1, 2]))
    assert d1 == d2
    d1, d2 = strip_dict_params(fig.data[1], Scatter(x=[1, 2, 3], y=[3, 2, 1]))
    assert d1 == d2


@skip('See https://github.com/plotly/python-api/issues/291')
def test_update_list_make_copies_false():
    trace1 = Scatter(x=[1, 2, 3], y=[2, 1, 2])
    trace2 = Scatter(x=[1, 2, 3], y=[3, 2, 1])
    data = Data([trace1, trace2])
    update = dict(x=[2, 3, 4], y=[1, 2, 3], line=Line())
    data.update(update, make_copies=False)
    assert data[0]['line'] is data[1]['line']
