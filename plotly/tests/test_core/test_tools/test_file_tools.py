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
