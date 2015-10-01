import os

# file structure
PLOTLY_DIR = os.path.join(os.path.expanduser("~"), ".plotly")
CREDENTIALS_FILE = os.path.join(PLOTLY_DIR, ".credentials")
CONFIG_FILE = os.path.join(PLOTLY_DIR, ".config")
GRAPH_REFERENCE_FILE = os.path.join(PLOTLY_DIR, ".graph_reference")
TEST_DIR = os.path.join(os.path.expanduser("~"), ".test")
TEST_FILE = os.path.join(PLOTLY_DIR, ".permission_test")

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

try:
    os.mkdir(TEST_DIR)
    os.rmdir(TEST_DIR)
    if not os.path.exists(PLOTLY_DIR):
        os.mkdir(PLOTLY_DIR)
    f = open(TEST_FILE, 'w')
    f.write('testing\n')
    f.close()
    os.remove(TEST_FILE)
    _file_permissions = True
except:
    _file_permissions = False


def check_file_permissions():
    return _file_permissions
