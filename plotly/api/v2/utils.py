from __future__ import absolute_import

import requests
from requests.compat import json as _json
from requests.exceptions import RequestException

from plotly import config, exceptions, version, utils
from plotly.api.utils import basic_auth


def make_params(**kwargs):
    """
    Helper to create a params dict, skipping undefined entries.

    :returns: (dict) A params dict to pass to `request`.

    """
    return {k: v for k, v in kwargs.items() if v is not None}


def build_url(resource, id='', route=''):
    """
    Create a url for a request on a V2 resource.

    :param (str) resource: E.g., 'files', 'plots', 'grids', etc.
    :param (str) id: The unique identifier for the resource.
    :param (str) route: Detail/list route. E.g., 'restore', 'lookup', etc.
    :return: (str) The url.

    """
    base = config.get_config()['plotly_api_domain']
    formatter = {'base': base, 'resource': resource, 'id': id, 'route': route}

    # Add path to base url depending on the input params. Note that `route`
    # can refer to a 'list' or a 'detail' route. Since it cannot refer to
    # both at the same time, it's overloaded in this function.
    if id:
        if route:
            url = '{base}/v2/{resource}/{id}/{route}'.format(**formatter)
        else:
            url = '{base}/v2/{resource}/{id}'.format(**formatter)
    else:
        if route:
            url = '{base}/v2/{resource}/{route}'.format(**formatter)
        else:
            url = '{base}/v2/{resource}'.format(**formatter)

    return url


def validate_response(response):
    """
    Raise a helpful PlotlyRequestError for failed requests.

    :param (requests.Response) response: A Response object from an api request.
    :raises: (PlotlyRequestError) If the request failed for any reason.
    :returns: (None)

    """
    if response.ok:
        return

    content = response.content
    status_code = response.status_code
    try:
        parsed_content = response.json()
    except ValueError:
        message = content if content else 'No Content'
        raise exceptions.PlotlyRequestError(message, status_code, content)

    message = ''
    if isinstance(parsed_content, dict):
        errors = parsed_content.get('errors', [])
        messages = [error.get('message') for error in errors]
        message = '\n'.join([msg for msg in messages if msg])
    if not message:
        message = content if content else 'No Content'

    raise exceptions.PlotlyRequestError(message, status_code, content)


def get_headers():
    """
    Using session credentials/config, get headers for a V2 API request.

    Users may have their own proxy layer and so we free up the `authorization`
    header for this purpose (instead adding the user authorization in a new
    `plotly-authorization` header). See pull #239.

    :returns: (dict) Headers to add to a requests.request call.

    """
    creds = config.get_credentials()

    headers = {
        'plotly-client-platform': 'python {}'.format(version.__version__),
        'content-type': 'application/json'
    }

    plotly_auth = basic_auth(creds['username'], creds['api_key'])
    proxy_auth = basic_auth(creds['proxy_username'], creds['proxy_password'])

    if config.get_config()['plotly_proxy_authorization']:
        headers['authorization'] = proxy_auth
        if creds['username'] and creds['api_key']:
            headers['plotly-authorization'] = plotly_auth
    else:
        if creds['username'] and creds['api_key']:
            headers['authorization'] = plotly_auth

    return headers


def request(method, url, **kwargs):
    """
    Central place to make any api v2 api request.

    :param (str) method: The request method ('get', 'put', 'delete', ...).
    :param (str) url: The full api url to make the request to.
    :param kwargs: These are passed along (but possibly mutated) to requests.
    :return: (requests.Response) The response directly from requests.

    """
    kwargs['headers'] = dict(kwargs.get('headers', {}), **get_headers())

    # Change boolean params to lowercase strings. E.g., `True` --> `'true'`.
    # Just change the value so that requests handles query string creation.
    if isinstance(kwargs.get('params'), dict):
        kwargs['params'] = kwargs['params'].copy()
        for key in kwargs['params']:
            if isinstance(kwargs['params'][key], bool):
                kwargs['params'][key] = _json.dumps(kwargs['params'][key])

    # We have a special json encoding class for non-native objects.
    if kwargs.get('json') is not None:
        if kwargs.get('data'):
            raise exceptions.PlotlyError('Cannot supply data and json kwargs.')
        kwargs['data'] = _json.dumps(kwargs.pop('json'), sort_keys=True,
                                     cls=utils.PlotlyJSONEncoder)

    # The config file determines whether reuqests should *verify*.
    kwargs['verify'] = config.get_config()['plotly_ssl_verification']

    try:
        response = requests.request(method, url, **kwargs)
    except RequestException as e:
        # The message can be an exception. E.g., MaxRetryError.
        message = str(getattr(e, 'message', 'No message'))
        response = getattr(e, 'response', None)
        status_code = response.status_code if response else None
        content = response.content if response else 'No content'
        raise exceptions.PlotlyRequestError(message, status_code, content)
    validate_response(response)
    return response
