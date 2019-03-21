"""Interface to Plotly's /v2/plot-schema endpoints."""
from __future__ import absolute_import

from plotly.api.v2.utils import build_url, make_params, request

RESOURCE = 'plot-schema'


def retrieve(sha1, **kwargs):
    """
    Retrieve the most up-to-date copy of the plot-schema wrt the given hash.

    :param (str) sha1: The last-known hash of the plot-schema (or '').
    :returns: (requests.Response) Returns response directly from requests.

    """
    url = build_url(RESOURCE)
    params = make_params(sha1=sha1)
    return request('get', url, params=params, **kwargs)
