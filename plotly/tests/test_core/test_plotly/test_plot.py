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
import plotly.session

# username for tests: 'PlotlyImageTest'
# api_key for account: '786r5mecv0'


def setUp():
    py.sign_in('PlotlyImageTest', '786r5mecv0',
               plotly_domain='https://plot.ly',
               world_readable=True,
               sharing='public')


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
    def setUp(self):
        py.sign_in('PlotlyImageTest', '786r5mecv0',
                   plotly_domain='https://plot.ly')
        self.simple_figure = {'data': [{'x': [1, 2, 3], 'y': [2, 1, 2]}]}
        super(TestPlot, self).setUp()

    def test_plot_empty_data(self):
        py.sign_in('PlotlyImageTest', '786r5mecv0')
        self.assertRaises(PlotlyEmptyDataError, py.plot, [],
                          filename='plot_invalid')

    def test_plot_sharing_invalid_argument(self):

        # Raise an error if sharing argument is incorrect
        # correct arguments {'public, 'private', 'secret'}

        kwargs = {'filename': 'invalid-sharing-argument',
                  'sharing': 'privste'}

        with self.assertRaisesRegexp(
                PlotlyError,
                "The 'sharing' argument only accepts"):
            py.plot(self.simple_figure, **kwargs)

    def test_plot_world_readable_sharing_conflict_1(self):

        # Raise an error if world_readable=False but sharing='public'

        kwargs = {'filename': 'invalid-privacy-setting',
                  'world_readable': False,
                  'sharing': 'public'}

        with self.assertRaisesRegexp(
                PlotlyError,
                'setting your plot privacy to both public and private.'):
            py.plot(self.simple_figure, **kwargs)

    def test_plot_world_readable_sharing_conflict_2(self):

        # Raise an error if world_readable=True but sharing='secret'

        kwargs = {'filename': 'invalid-privacy-setting',
                  'world_readable': True,
                  'sharing': 'secret'}

        with self.assertRaisesRegexp(
                PlotlyError,
                'setting your plot privacy to both public and private.'):
            py.plot(self.simple_figure, **kwargs)

    def test_plot_option_logic_only_world_readable_given(self):

        # If sharing is not given and world_readable=False,
        # sharing should be set to private

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
                                      'sharing': 'private'}
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

        validate = True
        fig = tls.return_figure_from_figure_or_data(self.simple_figure,
                                                    validate)
        kwargs = {'filename': 'is_share_key_included',
                  'fileopt': 'overwrite',
                  'world_readable': False,
                  'sharing': 'secret'}
        response = py._send_to_plotly(fig, **kwargs)
        plot_url = response['url']

        self.assertTrue('share_key=' in plot_url)

    def test_plot_url_response_given_sharing_key(self):

        # Given share_key is requested, get request of the url should
        # be 200

        kwargs = {'filename': 'is_share_key_included',
                  'fileopt': 'overwrite',
                  'auto_open': False,
                  'world_readable': False,
                  'sharing': 'secret'}

        plot_url = py.plot(self.simple_figure, **kwargs)
        response = requests.get(plot_url)
        self.assertEqual(response.status_code, 200)

    def test_private_plot_response_with_and_without_share_key(self):

        # The json file of the private plot should be 404 and once
        # share_key is added it should be 200

        kwargs = {'filename': 'is_share_key_included',
                  'fileopt': 'overwrite',
                  'world_readable': False,
                  'sharing': 'private'}

        private_plot_url = py._send_to_plotly(self.simple_figure,
                                              **kwargs)['url']
        private_plot_response = requests.get(private_plot_url + ".json")

        # The json file of the private plot should be 404
        self.assertEqual(private_plot_response.status_code, 404)

        secret_plot_url = py.add_share_key_to_url(private_plot_url)
        urlsplit = six.moves.urllib.parse.urlparse(secret_plot_url)
        secret_plot_json_file = six.moves.urllib.parse.urljoin(
            urlsplit.geturl(), "?.json" + urlsplit.query)
        secret_plot_response = requests.get(secret_plot_json_file)

        # The json file of the secret plot should be 200
        self.assertTrue(secret_plot_response.status_code, 200)


class TestPlotOptionLogic(TestCase):
    def tearDown(self):
        plotly.session._session['credentials'] = {}
        plotly.session._session['config'] = {}
        plotly.session._session['plot_options'] = {}
        py.sign_in('PlotlyImageTest', '786r5mecv0')
        tls.set_config_file(world_readable=True, sharing='public')

    def test_default_options(self):
        options = py._plot_option_logic({})
        config_options = tls.get_config_file()
        for key in options:
            if key != 'fileopt' and key in config_options:
                self.assertEqual(options[key], config_options[key])

    def test_signin_updates_options(self):
        config_options = tls.get_config_file()

        user_options = {
            'auto_open': not config_options['auto_open'],
            'world_readable': not config_options['world_readable'],
            'sharing': ('secret' if config_options['sharing'] != 'secret'
                        else 'private')
        }
        py.sign_in('username', 'api_key', **user_options)
        options = py._plot_option_logic({})

        # reload config_options to make sure that no mutation happened
        config_options = tls.get_config_file()

        for key in user_options:
            self.assertEqual(options[key], user_options[key])
            self.assertNotEqual(options[key], config_options[key])

    def test_call_signature_arguments_updates_options(self):
        config_options = tls.get_config_file()

        user_options = {
            'auto_open': not config_options['auto_open'],
            'world_readable': not config_options['world_readable']
        }
        if user_options['world_readable']:
            user_options['sharing'] = 'public'
        else:
            user_options['sharing'] = 'private'

        options = py._plot_option_logic(user_options)
        for key in user_options:
            self.assertEqual(options[key], user_options[key])

    def test_call_signature_overrides_signin_and_config_file(self):
        config_options = tls.get_config_file()

        signin_options = {
            'auto_open': not config_options['auto_open'],
            'world_readable': not config_options['world_readable'],
            'sharing': ('public' if config_options['world_readable'] is False
                        else 'secret')
        }

        call_signature_options = {
            'auto_open': config_options['auto_open'],
            'world_readable': config_options['world_readable']
        }
        if call_signature_options['world_readable'] is True:
            call_signature_options['sharing'] = 'public'
        elif config_options['sharing'] == 'secret':
            call_signature_options['sharing'] = 'private'
        else:
            call_signature_options['sharing'] = 'secret'

        py.sign_in('username', 'api_key', **signin_options)
        options = py._plot_option_logic(call_signature_options)
        for key in signin_options:
            self.assertNotEqual(signin_options[key], options[key])

    def test_set_config_updates_plot_options(self):
        original_config = tls.get_config_file()
        new_options = {
            'world_readable': not original_config['world_readable'],
            'auto_open': not original_config['auto_open'],
            'sharing': ('public' if original_config['world_readable'] is False
                        else 'secret')
        }
        tls.set_config_file(**new_options)
        options = py._plot_option_logic({})
        for key in new_options:
            self.assertEqual(new_options[key], options[key])
        tls.set_config_file(**original_config)

    def test_private_sharing_and_public_world_readable_conflict(self):
        """ If you supply an invalid combination at the same time,
        ie through sign_in, set_config, or through the call signature,
        then check that an error is raised.
        Otherwise, use whichever world_readable or sharing option has
        the highest precendence
        """

        self.assertRaises(PlotlyError, py._plot_option_logic,
                          {'world_readable': True, 'sharing': 'secret'})
        self.assertRaises(PlotlyError, py._plot_option_logic,
                          {'world_readable': True, 'sharing': 'private'})
        self.assertRaises(PlotlyError, py._plot_option_logic,
                          {'world_readable': False, 'sharing': 'public'})

        py.sign_in('username', 'key', world_readable=True, sharing='secret')
        self.assertRaises(PlotlyError, py._plot_option_logic, {})
        self.tearDown()

        py.sign_in('username', 'key', world_readable=True, sharing='private')
        self.assertRaises(PlotlyError, py._plot_option_logic, {})
        self.tearDown()

        py.sign_in('username', 'key', world_readable=False, sharing='public')
        self.assertRaises(PlotlyError, py._plot_option_logic, {})
        self.tearDown()

        self.assertRaises(PlotlyError, tls.set_config_file,
                          **dict(world_readable=True, sharing='secret'))
        self.tearDown()

        self.assertRaises(PlotlyError, tls.set_config_file,
                          world_readable=True, sharing='private')
        self.tearDown()

        self.assertRaises(PlotlyError, tls.set_config_file,
                          world_readable=False, sharing='public')
        self.tearDown()

        # But, precedence overwrites the options, no errors are raised
        py.sign_in('username', 'key', world_readable=True)
        options = py._plot_option_logic({'sharing': 'secret'})
        self.assertEqual(options['sharing'], 'secret')
        self.assertEqual(options['world_readable'], False)
        self.tearDown()

        py.sign_in('username', 'key', world_readable=True)
        options = py._plot_option_logic({'sharing': 'private'})
        self.assertEqual(options['sharing'], 'private')
        self.assertEqual(options['world_readable'], False)
        self.tearDown()

        py.sign_in('username', 'key', world_readable=False)
        options = py._plot_option_logic({'sharing': 'public'})
        self.assertEqual(options['sharing'], 'public')
        self.assertEqual(options['world_readable'], True)
        self.tearDown()

        tls.set_config_file(world_readable=True)
        options = py._plot_option_logic({'sharing': 'secret'})
        self.assertEqual(options['sharing'], 'secret')
        self.assertEqual(options['world_readable'], False)
        self.tearDown()

        tls.set_config_file(world_readable=True)
        options = py._plot_option_logic({'sharing': 'private'})
        self.assertEqual(options['sharing'], 'private')
        self.assertEqual(options['world_readable'], False)
        self.tearDown()

        tls.set_config_file(world_readable=False)
        options = py._plot_option_logic({'sharing': 'public'})
        self.assertEqual(options['sharing'], 'public')
        self.assertEqual(options['world_readable'], True)
        self.tearDown()
