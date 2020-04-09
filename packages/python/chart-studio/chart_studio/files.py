from __future__ import absolute_import

import os

# file structure
from _plotly_utils.files import PLOTLY_DIR

CREDENTIALS_FILE = os.path.join(PLOTLY_DIR, ".credentials")
CONFIG_FILE = os.path.join(PLOTLY_DIR, ".config")

# this sets both the DEFAULTS and the TYPES for these files
FILE_CONTENT = {
    CREDENTIALS_FILE: {
        "username": "",
        "api_key": "",
        "proxy_username": "",
        "proxy_password": "",
        "stream_ids": [],
    },
    CONFIG_FILE: {
        "plotly_domain": "https://plotly.com",
        "plotly_streaming_domain": "stream.plotly.com",
        "plotly_api_domain": "https://api.plotly.com",
        "plotly_ssl_verification": True,
        "plotly_proxy_authorization": False,
        "world_readable": True,
        "sharing": "public",
        "auto_open": True,
    },
}
