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

    def test_plot_sharing_argument(self):

        # Raise an error if sharing argument is incorrect
        # correct arguments {'public, 'private', 'secret'}

        fig = {
            'data': [
                {
                    'x': [1, 2, 3],
                    'y': [2, 1, 2]
                }
            ]
        }

        kwargs = {'filename': 'invalid-sharing-argument',
                  'sharing': 'privste'}
        self.assertRaises(PlotlyError, py.plot, fig, **kwargs)

    def test_plot_world_readable_sharing_conflict_1(self):

        # Raise an error if world_readable=False but sharing='public'

        fig = {
            'data': [
                {
                    'x': [1, 2, 3],
                    'y': [2, 1, 2]
                }
            ]
        }

        kwargs = {'filename': 'invalid-privacy-setting',
                  'world_readable': False,
                  'sharing': 'public'}
        self.assertRaises(PlotlyError, py.plot, fig, **kwargs)

    def test_plot_world_readable_sharing_conflict_2(self):

        # Raise an error if world_readable=True but sharing='secret'

        fig = {
            'data': [
                {
                    'x': [1, 2, 3],
                    'y': [2, 1, 2]
                }
            ]
        }

        kwargs = {'filename': 'invalid-privacy-setting',
                  'world_readable': True,
                  'sharing': 'secret'}
        self.assertRaises(PlotlyError, py.plot, fig, **kwargs)

    def test_plot_option_logic_only_world_readable_given(self):

        # If sharing is not given and world_readable=False,
        # sharing should be set to None

        kwargs = {'filename': 'test',
                  'auto_open': True,
                  'fileopt': 'overwrite',
                  'validate': True,
                  'world_readable': False}

        plot_option_logic = py._plot_option_logic(kwargs)

        expected_plot_option_logic = {'filename': 'test',
                                      'auto_open': True,
                                      'fileopt': 'overwrite',
                                      'validate': True,
                                      'world_readable': False,
                                      'sharing': None}
        self.assertEqual(plot_option_logic, expected_plot_option_logic)

    def test_plot_option_logic_only_sharing_given(self):

        # If world_readable is not given and sharing ='private',
        # world_readable should be set to False

        kwargs = {'filename': 'test',
                  'auto_open': True,
                  'fileopt': 'overwrite',
                  'validate': True,
                  'sharing': 'private'}

        plot_option_logic = py._plot_option_logic(kwargs)

        expected_plot_option_logic = {'filename': 'test',
                                      'auto_open': True,
                                      'fileopt': 'overwrite',
                                      'validate': True,
                                      'world_readable': False,
                                      'sharing': 'private'}
        self.assertEqual(plot_option_logic, expected_plot_option_logic)
