"""
test_plot:
==========

A module intended for use with Nose.

"""
from __future__ import absolute_import

import requests
import six

from unittest import TestCase
from nose.tools import raises

import plotly.tools as tls
from plotly.plotly import plotly as py
from plotly.exceptions import PlotlyError, PlotlyEmptyDataError


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

        with self.assertRaisesRegexp(PlotlyError, 'sharing'):
            py.plot(fig, **kwargs)

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

        with self.assertRaisesRegexp(PlotlyError, 'sharing'):
            py.plot(fig, **kwargs)

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

        with self.assertRaisesRegexp(PlotlyError, 'sharing'):
            py.plot(fig, **kwargs)

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

    def test_plot_url_given_sharing_key(self):

        # Give share_key is requested, the retun url should contain
        # the share_key

        data = {
            'data': [
                {
                    'x': [1, 2, 3],
                    'y': [2, 1, 2]
                }
            ]
        }
        validate = True
        fig = tls.return_figure_from_figure_or_data(data, validate)
        kwargs = {'filename': 'is_share_key_included',
                  'fileopt': 'overwrite',
                  'world_readable': False,
                  'sharing': 'secret'}
        response = py._send_to_plotly(fig, **kwargs)
        plot_url = response['url']

        self.assertTrue('share_key=' in plot_url)

    def test_plot_url_response_given_sharing_key(self):

        # Give share_key is requested, the get request of url should
        # be 200

        data = {
            'data': [
                {
                    'x': [1, 2, 3],
                    'y': [2, 1, 2]
                }
            ]
        }
        validate = True
        fig = tls.return_figure_from_figure_or_data(data, validate)
        kwargs = {'filename': 'is_share_key_included',
                  'fileopt': 'overwrite',
                  'world_readable': False,
                  'sharing': 'secret'}

        self.assertTrue(200 ==
                        requests.get(
                            py._send_to_plotly(fig, **kwargs)['url'])
                        .status_code)

    def test_private_plot_response_with_and_without_share_key(self):

        # The get response of private plot should be 404 and once share_key
        # is added it should be 200

        data = {
            'data': [
                {
                    'x': [1, 2, 3],
                    'y': [2, 1, 2]
                }
            ]
        }
        validate = True
        fig = tls.return_figure_from_figure_or_data(data, validate)
        kwargs = {'filename': 'is_share_key_included',
                  'fileopt': 'overwrite',
                  'world_readable': False,
                  'sharing': 'private'}

        private_plot_url = py._send_to_plotly(fig, **kwargs)['url']

        self.assertTrue(404 ==
                        requests.get(private_plot_url + ".json").status_code)

        secret_plot_url = py.add_share_key_to_url(private_plot_url)
        urlsplit = six.moves.urllib.parse.urlparse(secret_plot_url)
        secret_plot_url_in_json = six.moves.urllib.parse.urljoin(
            urlsplit.geturl(), "?.json" + urlsplit.query)
        self.assertTrue(200 ==
                        requests.get(secret_plot_url_in_json).status_code)
