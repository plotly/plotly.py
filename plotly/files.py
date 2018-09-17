import os
from stat import ST_MODE, S_IWUSR, S_IRUSR

# file structure
PLOTLY_DIR = os.path.join(os.path.expanduser("~"), ".plotly")
CREDENTIALS_FILE = os.path.join(PLOTLY_DIR, ".credentials")
CONFIG_FILE = os.path.join(PLOTLY_DIR, ".config")

# this sets both the DEFAULTS and the TYPES for these files
FILE_CONTENT = {CREDENTIALS_FILE: {'username': '',
                                   'api_key': '',
                                   'proxy_username': '',
                                   'proxy_password': '',
                                   'stream_ids': []},
                CONFIG_FILE: {'plotly_domain': 'https://plot.ly',
                              'plotly_streaming_domain': 'stream.plot.ly',
                              'plotly_api_domain': 'https://api.plot.ly',
                              'plotly_ssl_verification': True,
                              'plotly_proxy_authorization': False,
                              'world_readable': True,
                              'sharing': 'public',
                              'auto_open': True}}


def _permissions():
    try:
        if not os.path.exists(PLOTLY_DIR):
            os.mkdir(PLOTLY_DIR)
        return os.stat(PLOTLY_DIR)[ST_MODE] & (S_IWUSR | S_IRUSR) == (S_IWUSR | S_IRUSR)
    except:
        return False


_file_permissions = _permissions()


def check_file_permissions():
    return _file_permissions
