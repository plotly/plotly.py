import plotly.plotly.plotly as py
import plotly.tools as tls


def test_get_credentials():
    if 'username' in py._credentials:
        del py._credentials['username']
    if 'api_key' in py._credentials:
        del py._credentials['api_key']
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