from __future__ import absolute_import

from unittest import TestCase

import plotly.plotly.plotly as py
import plotly.session as session
import plotly.tools as tls


def test_get_credentials():
    session_credentials = session.get_session_credentials()
    if 'username' in session_credentials:
        del session._session['credentials']['username']
    if 'api_key' in session_credentials:
        del session._session['credentials']['api_key']
    creds = py.get_credentials()
    file_creds = tls.get_credentials_file()
    print(creds)
    print(file_creds)
    assert creds == file_creds


def test_sign_in():
    un = 'anyone'
    ak = 'something'
    # TODO, add this!
    # si = ['this', 'and-this']
    py.sign_in(un, ak)
    creds = py.get_credentials()
    assert creds['username'] == un
    assert creds['api_key'] == ak
    # TODO, and check it!
    # assert creds['stream_ids'] == si


class TestSignIn(TestCase):

    def test_get_config(self):
        plotly_domain = 'test domain'
        plotly_streaming_domain = 'test streaming domain'
        config1 = py.get_config()
        session._session['config']['plotly_domain'] = plotly_domain
        config2 = py.get_config()
        session._session['config']['plotly_streaming_domain'] = (
            plotly_streaming_domain
        )
        config3 = py.get_config()
        self.assertEqual(config2['plotly_domain'], plotly_domain)
        self.assertNotEqual(
            config2['plotly_streaming_domain'], plotly_streaming_domain
        )
        self.assertEqual(
            config3['plotly_streaming_domain'], plotly_streaming_domain
        )

    def test_sign_in_with_config(self):
        username = 'place holder'
        api_key = 'place holder'
        plotly_domain = 'test domain'
        plotly_streaming_domain = 'test streaming domain'
        plotly_ssl_verification = False
        py.sign_in(
            username,
            api_key,
            plotly_domain=plotly_domain,
            plotly_streaming_domain=plotly_streaming_domain,
            plotly_ssl_verification=plotly_ssl_verification
        )
        config = py.get_config()
        self.assertEqual(config['plotly_domain'], plotly_domain)
        self.assertEqual(
            config['plotly_streaming_domain'], plotly_streaming_domain
        )
        self.assertEqual(
            config['plotly_ssl_verification'], plotly_ssl_verification
        )
