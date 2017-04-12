"""
Beta interface to Plotly's /v2/dash-apps endpoints.
"""
from __future__ import absolute_import

from plotly.api.v2.utils import build_url, request

RESOURCE = 'dash-apps'


def create(body):
    """Create a dash app item."""
    url = build_url(RESOURCE)
    return request('post', url, json=body)


def retrieve(fid):
    """Retrieve a dash app from Plotly."""
    url = build_url(RESOURCE, id=fid)
    return request('get', url)


def update(fid, content):
    """Completely update the writable."""
    url = build_url(RESOURCE, id=fid)
    return request('put', url, json=content)
