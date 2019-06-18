"""Interface to Plotly's /v2/files endpoints."""
from __future__ import absolute_import

from chart_studio.api.v2.utils import build_url, request

RESOURCE = "users"


def current():
    """
    Retrieve information on the logged-in user from Plotly.

    :returns: (requests.Response) Returns response directly from requests.

    """
    url = build_url(RESOURCE, route="current")
    return request("get", url)
