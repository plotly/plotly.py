"""
test_plot:
==========

A module intended for use with Nose.

"""
from __future__ import absolute_import
from nose.tools import raises

from plotly.graph_objs import graph_objs
from plotly.plotly import plotly as py
from plotly.exceptions import PlotlyError


# username for tests: 'plotlyimagetest'
# api_key for account: '786r5mecv0'


def plot_valid():
    fig = {
        'data':[
            {
                'x':[1,2,3],
                'y':[2,1,2],
                'z':[3,4,1]
            }
        ]
    }
    url = py.plot(fig, auto_open=False, filename='plot_valid')


@raises(PlotlyError)
def plot_invalid():
    fig = {
        'data':[
            {
                'x':[1,2,3],
                'y':[2,1,2],
                'z':[3,4,1]
            }
        ]
    }
    url = py.plot(fig, auto_open=False, filename='plot_invalid')


def test_bar():
    pass


def test_box():
    pass


def test_contour():
    pass


def test_heatmap():
    pass


def test_histogram():
    pass


def test_histogram2d():
    pass


def test_histogram2dcontour():
    pass


def test_plot_scatter():
    pass