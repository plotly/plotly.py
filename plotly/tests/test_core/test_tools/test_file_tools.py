<<<<<<< HEAD
<<<<<<< HEAD
from unittest import TestCase

from plotly import tools, session
||||||| merged common ancestors
from unittest import TestCase

from plotly import tools
from plotly import session
=======
from plotly import tools
from plotly import session
from plotly.tests.utils import PlotlyTestCase
>>>>>>> 6f2eb8a4d210809121fe7536e2150ff8f30b8168


class FileToolsTest(PlotlyTestCase):

    def test_set_config_file_all_entries(self):

        # Check set_config and get_config return the same values

        pd, ps, pa = 'this', 'thing', 'that'
        psv = False
        po = {'world_readable': False}
        tools.set_config_file(plotly_domain=pd,
                              plotly_streaming_domain=ps,
                              plotly_api_domain=pa,
                              plotly_ssl_verification=psv,
                              plot_options=po)
        config = tools.get_config_file()
        self.assertEqual(config['plotly_domain'], pd)
        self.assertEqual(config['plotly_streaming_domain'], ps)
        self.assertEqual(config['plotly_api_domain'], pa)
        self.assertEqual(config['plotly_ssl_verification'], psv)
        self.assertEqual(config['plot_options'], po)

    def test_set_config_file_two_entries(self):

        # Check set_config and get_config given only two entries return the
        # same values

        pd, ps = 'this', 'thing'
        tools.set_config_file(plotly_domain=pd, plotly_streaming_domain=ps)
        config = tools.get_config_file()
        self.assertEqual(config['plotly_domain'], pd)
        self.assertEqual(config['plotly_streaming_domain'], ps)

    def test_session_plot_option(self):

        # Check if the session_plot_option and config_plot_optin return the
        # same value

        po = {'world_readable': True}
        tools.set_config_file(plot_options=po)
        session_po = session.get_session_plot_options()
        self.assertEqual(session_po['world_readable'], po['world_readable'])

    def test_set_config_file_plot_option(self):

        # Return TypeError when plot_option type is not a dict

        kwargs = {'plot_option': False}
        self.assertRaises(TypeError, tools.set_config_file, **kwargs)

    def test_reset_config_file(self):

        # Check reset_config and get_config return the same values

        tools.reset_config_file()
        config = tools.get_config_file()
        self.assertEqual(config['plotly_domain'], 'https://plot.ly')
        self.assertEqual(config['plotly_streaming_domain'], 'stream.plot.ly')

    def test_get_credentials_file(self):

        # Check get_credentials returns all the keys

        original_creds = tools.get_credentials_file()
        expected = ['username', 'stream_ids', 'api_key']
        self.assertTrue(all(x in original_creds for x in expected))

    def test_reset_credentials_file(self):

        # Check get_cred return all the keys

        tools.reset_credentials_file()
        reset_creds = tools.get_credentials_file()
        expected = ['username', 'stream_ids', 'api_key']
        self.assertTrue(all(x in reset_creds for x in expected))
||||||| merged common ancestors
import plotly.tools as tls


def test_reset_config_file():
    tls.reset_config_file()
    config = tls.get_config_file()
    assert config['plotly_domain'] == 'https://plot.ly'
    assert config['plotly_streaming_domain'] == 'stream.plot.ly'


def test_set_config_file():
    pd, ps = 'this', 'thing'
    tls.set_config_file(plotly_domain=pd, plotly_streaming_domain=ps)
    config = tls.get_config_file()
    assert config['plotly_domain'] == pd
    assert config['plotly_streaming_domain'] == ps
    tls.reset_config_file()  # else every would hate me :)


def test_credentials_tools():
    original_creds = tls.get_credentials_file()
    expected = ['username', 'stream_ids', 'api_key']
    assert all(x in original_creds for x in expected)
    # now, if that worked, we can try this!
    tls.reset_credentials_file()
    reset_creds = tls.get_credentials_file()
    tls.set_credentials_file(**original_creds)
    assert all(x in reset_creds for x in expected)
    creds = tls.get_credentials_file()
    assert all(x in creds for x in expected)
    assert original_creds == creds
=======
from __future__ import absolute_import

import plotly.tools as tls


def test_reset_config_file():
    tls.reset_config_file()
    config = tls.get_config_file()
    assert config['plotly_domain'] == 'https://plot.ly'
    assert config['plotly_streaming_domain'] == 'stream.plot.ly'


def test_set_config_file():
    pd, ps = 'this', 'thing'
    ssl_verify, proxy_auth = True, True
    tls.set_config_file(plotly_domain=pd, plotly_streaming_domain=ps,
                        plotly_ssl_verification=ssl_verify,
                        plotly_proxy_authorization=proxy_auth)
    config = tls.get_config_file()
    assert config['plotly_domain'] == pd
    assert config['plotly_streaming_domain'] == ps
    assert config['plotly_ssl_verification'] == ssl_verify
    assert config['plotly_proxy_authorization'] == proxy_auth
    tls.reset_config_file()  # else every would hate me :)


def test_credentials_tools():
    original_creds = tls.get_credentials_file()
    expected = ['username', 'stream_ids', 'api_key', 'proxy_username',
                'proxy_password']
    assert all(x in original_creds for x in expected)

    # now, if that worked, we can try this!
    tls.reset_credentials_file()
    reset_creds = tls.get_credentials_file()
    tls.set_credentials_file(**original_creds)
    assert all(x in reset_creds for x in expected)
    creds = tls.get_credentials_file()
    assert all(x in creds for x in expected)
    assert original_creds == creds
>>>>>>> afe8b56bb06320a90ce3a404264bc8b3060b87da
