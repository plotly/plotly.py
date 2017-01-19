"""Interface to Plotly's /v2/plots endpoints."""
from __future__ import absolute_import

from plotly.api.v2.utils import build_url, make_params, request

RESOURCE = 'plots'


def create(body):
    """
    Create a new plot.

    :param (dict) body: A mapping of body param names to values.
    :returns: (requests.Response) Returns response directly from requests.

    """
    url = build_url(RESOURCE)
    return request('post', url, json=body)


def retrieve(fid, share_key=None):
    """
    Retrieve a plot from Plotly.

    :param (str) fid: The `{username}:{idlocal}` identifier. E.g. `foo:88`.
    :param (str) share_key: The secret key granting 'read' access if private.
    :returns: (requests.Response) Returns response directly from requests.

    """
    url = build_url(RESOURCE, id=fid)
    params = make_params(share_key=share_key)
    return request('get', url, params=params)


def content(fid, share_key=None, inline_data=None, map_data=None):
    """
    Retrieve the *figure* for a Plotly plot file.

    :param (str) fid: The `{username}:{idlocal}` identifier. E.g. `foo:88`.
    :param (str) share_key: The secret key granting 'read' access if private.
    :param (bool) inline_data: If True, include the data arrays with the plot.
    :param (str) map_data: Currently only accepts 'unreadable' to return a
                           mapping of grid-fid: grid. This is useful if you
                           want to maintain structure between the plot and
                           referenced grids when you have READ access to the
                           plot, but you don't have READ access to the
                           underlying grids.
    :returns: (requests.Response) Returns response directly from requests.

    """
    url = build_url(RESOURCE, id=fid, route='content')
    params = make_params(share_key=share_key, inline_data=inline_data,
                         map_data=map_data)
    return request('get', url, params=params)


def update(fid, body):
    """
    Update a plot from Plotly.

    :param (str) fid: The `{username}:{idlocal}` identifier. E.g. `foo:88`.
    :param (dict) body: A mapping of body param names to values.
    :returns: (requests.Response) Returns response directly from requests.

    """
    url = build_url(RESOURCE, id=fid)
    return request('put', url, json=body)


def trash(fid):
    """
    Soft-delete a plot from Plotly. (Can be undone with 'restore').

    :param (str) fid: The `{username}:{idlocal}` identifier. E.g. `foo:88`.
    :returns: (requests.Response) Returns response directly from requests.

    """
    url = build_url(RESOURCE, id=fid, route='trash')
    return request('post', url)


def restore(fid):
    """
    Restore a trashed plot from Plotly. See 'trash'.

    :param (str) fid: The `{username}:{idlocal}` identifier. E.g. `foo:88`.
    :returns: (requests.Response) Returns response directly from requests.

    """
    url = build_url(RESOURCE, id=fid, route='restore')
    return request('post', url)


def permanent_delete(fid, params=None):
    """
    Permanently delete a trashed plot file from Plotly. See 'trash'.

    :param (str) fid: The `{username}:{idlocal}` identifier. E.g. `foo:88`.
    :returns: (requests.Response) Returns response directly from requests.

    """
    url = build_url(RESOURCE, id=fid, route='permanent_delete')
    return request('delete', url, params=params)


def lookup(path, parent=None, user=None, exists=None):
    """
    Retrieve a plot file from Plotly without needing a fid.

    :param (str) path: The '/'-delimited path specifying the file location.
    :param (int) parent: Parent id, an integer, which the path is relative to.
    :param (str) user: The username to target files for. Defaults to requestor.
    :param (bool) exists: If True, don't return the full file, just a flag.
    :returns: (requests.Response) Returns response directly from requests.

    """
    url = build_url(RESOURCE, route='lookup')
    params = make_params(path=path, parent=parent, user=user, exists=exists)
    return request('get', url, params=params)
