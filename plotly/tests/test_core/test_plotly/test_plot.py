"""
test_plot:
==========

A module intended for use with Nose.

"""
from __future__ import absolute_import

from unittest import TestCase

from nose.tools import raises

from plotly.exceptions import PlotlyError, PlotlyEmptyDataError
from plotly.plotly import plotly as py


# username for tests: 'PlotlyImageTest'
# api_key for account: '786r5mecv0'


def setUp():
    py.sign_in('PlotlyImageTest', '786r5mecv0',
               plotly_domain='https://plot.ly')


def test_plot_valid():
    fig = {
        'data': [
            {
                'x': [1, 2, 3],
                'y': [2, 1, 2]
            }
        ]
    }
    py.plot(fig, auto_open=False, filename='plot_valid')


@raises(PlotlyError)
def test_plot_invalid():
    fig = {
        'data': [
            {
                'x': [1, 2, 3],
                'y': [2, 1, 2],
                'z': [3, 4, 1]
            }
        ]
    }
    py.plot(fig, auto_open=False, filename='plot_invalid')


@raises(TypeError)
def test_plot_invalid_args_1():
    py.plot(x=[1, 2, 3], y=[2, 1, 2], auto_open=False, filename='plot_invalid')


@raises(PlotlyError)
def test_plot_invalid_args_2():
    py.plot([1, 2, 3], [2, 1, 2], auto_open=False, filename='plot_invalid')


class TestPlot(TestCase):

    def test_plot_empty_data(self):
        py.sign_in('PlotlyImageTest', '786r5mecv0')
        self.assertRaises(PlotlyEmptyDataError, py.plot, [],
                          filename='plot_invalid')
