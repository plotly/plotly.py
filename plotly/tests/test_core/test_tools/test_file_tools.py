from plotly import tools, session
from plotly.tests.utils import PlotlyTestCase

import warnings


class FileToolsTest(PlotlyTestCase):

    def test_set_config_file_all_entries(self):

        # Check set_config and get_config return the same values

        domain, streaming_domain, api, sharing = ('this', 'thing',
                                                  'that', 'private')
        ssl_verify, proxy_auth, world_readable, auto_open = (True, True,
                                                             False, False)
        tools.set_config_file(plotly_domain=domain,
                              plotly_streaming_domain=streaming_domain,
                              plotly_api_domain=api,
                              plotly_ssl_verification=ssl_verify,
                              plotly_proxy_authorization=proxy_auth,
                              world_readable=world_readable,
                              auto_open=auto_open)
        config = tools.get_config_file()
        self.assertEqual(config['plotly_domain'], domain)
        self.assertEqual(config['plotly_streaming_domain'], streaming_domain)
        self.assertEqual(config['plotly_api_domain'], api)
        self.assertEqual(config['plotly_ssl_verification'], ssl_verify)
        self.assertEqual(config['plotly_proxy_authorization'], proxy_auth)
        self.assertEqual(config['world_readable'], world_readable)
        self.assertEqual(config['sharing'], sharing)
        self.assertEqual(config['auto_open'], auto_open)
        tools.reset_config_file()

    def test_set_config_file_two_entries(self):

        # Check set_config and get_config given only two entries return the
        # same values

        domain, streaming_domain = 'this', 'thing'
        tools.set_config_file(plotly_domain=domain,
                              plotly_streaming_domain=streaming_domain)
        config = tools.get_config_file()
        self.assertEqual(config['plotly_domain'], domain)
        self.assertEqual(config['plotly_streaming_domain'], streaming_domain)
        tools.reset_config_file()

    def test_set_config_file_world_readable(self):

        # Return TypeError when world_readable type is not a bool

        kwargs = {'world_readable': 'True'}
        self.assertRaises(TypeError, tools.set_config_file, **kwargs)

    def test_set_config_expected_warning_msg(self):

        # Check that UserWarning is being called with http plotly_domain

        with warnings.catch_warnings(record=True) as w:
            warnings.simplefilter("always")
            kwargs = {'plotly_domain': 'http://www.foo-bar.com'}
            tools.set_config_file(**kwargs)
            assert len(w) == 1
            assert issubclass(w[-1].category, UserWarning)
            assert "plotly_domain" in str(w[-1].message)


    def test_set_config_no_warning_msg_if_plotly_domain_is_https(self):

        # Check that no UserWarning is being called with https plotly_domain

        with warnings.catch_warnings(record=True) as w:
            warnings.simplefilter("always")
            kwargs = {'plotly_domain': 'https://www.foo-bar.com'}
            tools.set_config_file(**kwargs)
            assert len(w) == 0


    def test_reset_config_file(self):

        # Check reset_config and get_config return the same values

        tools.reset_config_file()
        config = tools.get_config_file()
        self.assertEqual(config['plotly_domain'], 'https://plot.ly')
        self.assertEqual(config['plotly_streaming_domain'], 'stream.plot.ly')

    def test_get_credentials_file(self):

        # Check get_credentials returns all the keys

        original_creds = tools.get_credentials_file()
        expected = ['username', 'stream_ids', 'api_key', 'proxy_username',
                    'proxy_password']
        self.assertTrue(all(x in original_creds for x in expected))

    def test_reset_credentials_file(self):

        # Check get_cred return all the keys

        tools.reset_credentials_file()
        reset_creds = tools.get_credentials_file()
        expected = ['username', 'stream_ids', 'api_key', 'proxy_username',
                    'proxy_password']
        self.assertTrue(all(x in reset_creds for x in expected))
