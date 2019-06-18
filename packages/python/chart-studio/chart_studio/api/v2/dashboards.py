"""
Interface to Plotly's /v2/dashboards endpoints.

Partially complete at the moment. Only being used by
plotly.plotly.dashboard_ops.
"""
from __future__ import absolute_import

from chart_studio.api.v2.utils import build_url, request

RESOURCE = "dashboards"


def create(body):
    """Create a dashboard."""
    url = build_url(RESOURCE)
    return request("post", url, json=body)


def list():
    """Returns the list of all users' dashboards."""
    url = build_url(RESOURCE)
    return request("get", url)


def retrieve(fid):
    """Retrieve a dashboard from Plotly."""
    url = build_url(RESOURCE, id=fid)
    return request("get", url)


def update(fid, content):
    """Completely update the writable."""
    url = build_url(RESOURCE, id=fid)
    return request("put", url, json=content)


def schema():
    """Retrieve the dashboard schema."""
    url = build_url(RESOURCE, route="schema")
    return request("get", url)
