from __future__ import absolute_import

import requests
from requests.exceptions import RequestException
from retrying import retry

from plotly import config, exceptions
from plotly.api.utils import basic_auth
from plotly.api.v2.utils import should_retry


def validate_response(response):
    """
    Raise a helpful PlotlyRequestError for failed requests.

    :param (requests.Response) response: A Response object from an api request.
    :raises: (PlotlyRequestError) If the request failed for any reason.
    :returns: (None)

    """
    content = response.content
    status_code = response.status_code
    try:
        parsed_content = response.json()
    except ValueError:
        message = content if content else 'No Content'
        raise exceptions.PlotlyRequestError(message, status_code, content)

    message = ''
    if isinstance(parsed_content, dict):
        error = parsed_content.get('error')
        if error:
            message = error
        else:
            if response.ok:
                return
    if not message:
        message = content if content else 'No Content'

    raise exceptions.PlotlyRequestError(message, status_code, content)


def get_headers():
    """
    Using session credentials/config, get headers for a v1 API request.

    Users may have their own proxy layer and so we free up the `authorization`
    header for this purpose (instead adding the user authorization in a new
    `plotly-authorization` header). See pull #239.

    :returns: (dict) Headers to add to a requests.request call.

    """
    headers = {}
    creds = config.get_credentials()
    proxy_auth = basic_auth(creds['proxy_username'], creds['proxy_password'])

    if config.get_config()['plotly_proxy_authorization']:
        headers['authorization'] = proxy_auth

    return headers


@retry(wait_exponential_multiplier=1000, wait_exponential_max=16000,
       stop_max_delay=180000, retry_on_exception=should_retry)
def request(method, url, **kwargs):
    """
    Central place to make any v1 api request.

    :param (str) method: The request method ('get', 'put', 'delete', ...).
    :param (str) url: The full api url to make the request to.
    :param kwargs: These are passed along to requests.
    :return: (requests.Response) The response directly from requests.

    """
    if kwargs.get('json', None) is not None:
        # See plotly.api.v2.utils.request for examples on how to do this.
        raise exceptions.PlotlyError('V1 API does not handle arbitrary json.')
    kwargs['headers'] = dict(kwargs.get('headers', {}), **get_headers())
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
