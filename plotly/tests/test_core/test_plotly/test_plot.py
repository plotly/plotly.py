"""
test_plot:
==========

A module intended for use with Nose.

"""
from __future__ import absolute_import
from nose.tools import raises
from unittest import TestCase

from plotly.graph_objs import graph_objs
from plotly.plotly import plotly as py
from plotly.exceptions import PlotlyError, PlotlyEmptyDataError


# username for tests: 'PlotlyImageTest'
# api_key for account: '786r5mecv0'


def test_plot_valid():
    py.sign_in('PlotlyImageTest', '786r5mecv0')
    fig = {
        'data':[
            {
                'x':[1,2,3],
                'y':[2,1,2]
            }
        ]
    }
    url = py.plot(fig, auto_open=False, filename='plot_valid')


@raises(PlotlyError)
def test_plot_invalid():
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

@raises(TypeError)
def test_plot_invalid_args_1():
    url = py.plot(x=[1,2,3],
                  y=[2,1,2],
                  auto_open=False,
                  filename='plot_invalid')

@raises(PlotlyError)
def test_plot_invalid_args_2():
    url = py.plot([1,2,3], [2,1,2],
                  auto_open=False,
                  filename='plot_invalid')


class TestPlot(TestCase):

    def test_plot_empty_data(self):
        py.sign_in('PlotlyImageTest', '786r5mecv0')
        self.assertRaises(PlotlyEmptyDataError, py.plot, [],
                          filename='plot_invalid')


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
