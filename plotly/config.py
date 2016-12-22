"""
Merges and prioritizes file/session config and credentials.

This is promoted to its own module to simplify imports.

"""
from __future__ import absolute_import

from plotly import session, tools


def get_credentials():
    """Returns the credentials that will be sent to plotly."""
    credentials = tools.get_credentials_file()
    session_credentials = session.get_session_credentials()
    for credentials_key in credentials:

        # checking for not false, but truthy value here is the desired behavior
        session_value = session_credentials.get(credentials_key)
        if session_value is False or session_value:
            credentials[credentials_key] = session_value
    return credentials


def get_config():
    """Returns either module config or file config."""
    config = tools.get_config_file()
    session_config = session.get_session_config()
    for config_key in config:

        # checking for not false, but truthy value here is the desired behavior
        session_value = session_config.get(config_key)
        if session_value is False or session_value:
            config[config_key] = session_value
    return config
