"""
Interface to Plotly's /v2/spectacle-presentations endpoint.
"""
from __future__ import absolute_import

from plotly.api.v2.utils import build_url, request

RESOURCE = 'spectacle-presentations'


def create(body):
    """Create a presentation."""
    url = build_url(RESOURCE)
    return request('post', url, json=body)


def list():
    """Returns the list of all users' presentations."""
    url = build_url(RESOURCE)
    return request('get', url)


def retrieve(fid):
    """Retrieve a presentation from Plotly."""
    url = build_url(RESOURCE, id=fid)
    return request('get', url)


def update(fid, content):
    """Completely update the writable."""
    url = build_url(RESOURCE, id=fid)
    return request('put', url, json=content)
