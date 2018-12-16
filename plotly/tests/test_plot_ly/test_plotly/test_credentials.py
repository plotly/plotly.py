from __future__ import absolute_import

import plotly.plotly.plotly as py
import plotly.session as session
import plotly.tools as tls
from plotly import exceptions
from plotly.tests.utils import PlotlyTestCase

import sys

# import from mock
if sys.version_info.major == 3 and sys.version_info.minor >= 3:
    from unittest.mock import patch
else:
    from mock import patch


class TestSignIn(PlotlyTestCase):

    def setUp(self):
        super(TestSignIn, self).setUp()
        patcher = patch('plotly.api.v2.users.current')
        self.users_current_mock = patcher.start()
        self.addCleanup(patcher.stop)

    def test_get_credentials(self):
        session_credentials = session.get_session_credentials()
        if 'username' in session_credentials:
            del session._session['credentials']['username']
        if 'api_key' in session_credentials:
            del session._session['credentials']['api_key']
        creds = py.get_credentials()
        file_creds = tls.get_credentials_file()
        self.assertEqual(creds, file_creds)

    def test_sign_in(self):
        un = 'anyone'
        ak = 'something'
        # TODO, add this!
        # si = ['this', 'and-this']
        py.sign_in(un, ak)
        creds = py.get_credentials()
        self.assertEqual(creds['username'], un)
        self.assertEqual(creds['api_key'], ak)
        # TODO, and check it!
        # assert creds['stream_ids'] == si

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

    def test_sign_in_cannot_validate(self):
        self.users_current_mock.side_effect = exceptions.PlotlyRequestError(
            'msg', 400, 'foobar'
        )
        with self.assertRaisesRegexp(exceptions.PlotlyError, 'Sign in failed'):
            py.sign_in('foo', 'bar')
