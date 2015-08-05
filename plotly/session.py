"""
The session module handles the user's current credentials, config and plot opts

This allows users to dynamically change which plotly domain they're using,
which user they're signed in as, and plotting defaults.

"""
from __future__ import absolute_import

import copy

import six

from plotly import exceptions

_session = {
    'credentials': {},
    'config': {},
    'plot_options': {}
}

CREDENTIALS_KEYS = {
    'username': six.string_types,
    'api_key': six.string_types,
    'stream_ids': list
}

CONFIG_KEYS = {
    'plotly_domain': six.string_types,
    'plotly_streaming_domain': six.string_types,
    'plotly_api_domain': six.string_types,
    'plotly_ssl_verification': bool,
    'plotly_proxy_authorization': bool,
    'world_readable': bool
}

PLOT_OPTIONS = {
    'filename': six.string_types,
    'fileopt': six.string_types,
    'world_readable': bool,
    'auto_open': bool,
    'validate': bool,
    'sharing': six.string_types
}

SHARING_OPTIONS = ['public', 'private', 'secret']


def sign_in(username, api_key, **kwargs):
    """
    Set set session credentials and config (not saved to file).

    If unspecified, credentials and config are searched for in `.plotly` dir.

    :param (str) username: The username you'd use to sign in to Plotly
    :param (str) api_key: The api key associated with above username
    :param (list|optional) stream_ids: Stream tokens for above credentials
    :param (str|optional) proxy_username: The un associated with with your Proxy
    :param (str|optional) proxy_password: The pw associated with your Proxy un

    :param (str|optional) plotly_domain:
    :param (str|optional) plotly_streaming_domain:
    :param (str|optional) plotly_api_domain:
    :param (bool|optional) plotly_ssl_verification:
    :param (bool|optional) plotly_proxy_authorization:
    :param (bool|optional) world_readable:

    """
    # TODO: verify these _credentials with plotly

    # kwargs will contain all our info
    kwargs.update(username=username, api_key=api_key)

    # raise error if key isn't valid anywhere
    for key in kwargs:
        if key not in CREDENTIALS_KEYS and key not in CONFIG_KEYS:
            raise exceptions.PlotlyError(
                "{} is not a valid config or credentials key".format(key)
            )

    # add credentials, raise error if type is wrong.
    for key in CREDENTIALS_KEYS:
        if key in kwargs:
            if not isinstance(kwargs[key], CREDENTIALS_KEYS[key]):
                raise exceptions.PlotlyError(
                    "{} must be of type '{}'"
                    .format(key, CREDENTIALS_KEYS[key])
                )
            _session['credentials'][key] = kwargs[key]

    # add config, raise error if type is wrong.
    for key in CONFIG_KEYS:
        if key in kwargs:
            if not isinstance(kwargs[key], CONFIG_KEYS[key]):
                raise exceptions.PlotlyError("{} must be of type '{}'"
                                             .format(key, CONFIG_KEYS[key]))
            _session['config'][key] = kwargs.get(key)


def update_session_plot_options(**kwargs):
    """
    Update the _session plot_options

    :param (str|optional) filename: What the file will be named in Plotly
    :param (str|optional) fileopt: 'overwrite', 'append', 'new', or 'extend'
    :param (bool|optional) world_readable: Make public or private.
    :param (dict|optional) sharing: 'public', 'private', 'secret'
    :param (bool|optional) auto_open: For `plot`, open in new browser tab?
    :param (bool|optional) validate: Error locally if data doesn't pass?

    """
    # raise exception if key is invalid or value is the wrong type
    for key in kwargs:
        if key not in PLOT_OPTIONS:
            raise exceptions.PlotlyError(
                "{} is not a valid config or plot option key".format(key)
            )
        if not isinstance(kwargs[key], PLOT_OPTIONS[key]):
            raise exceptions.PlotlyError("{} must be of type '{}'"
                                         .format(key, PLOT_OPTIONS[key]))

        # raise exception if sharing is invalid
        if (key == 'sharing' and not (kwargs[key] in SHARING_OPTIONS)):
            raise exceptions.PlotlyError("'{0}' must be of either '{1}', '{2}'"
                                         " or '{3}'"
                                         .format(key, *SHARING_OPTIONS))

    # update local _session dict with new plot options
    _session['plot_options'].update(kwargs)


def get_session_plot_options():
    """ Returns a copy of the user supplied plot options.
    Use `update_plot_options()` to change.
    """
    return copy.deepcopy(_session['plot_options'])


def get_session_config():
    """Returns either module config or file config."""
    return copy.deepcopy(_session['config'])


def get_session_credentials():
    """Returns the credentials that will be sent to plotly."""
    return copy.deepcopy(_session['credentials'])
