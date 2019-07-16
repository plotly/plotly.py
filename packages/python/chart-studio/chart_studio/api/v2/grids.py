"""Interface to Plotly's /v2/grids endpoints."""
from __future__ import absolute_import

from chart_studio.api.v2.utils import build_url, make_params, request

RESOURCE = "grids"


def create(body):
    """
    Create a new grid.

    :param (dict) body: A mapping of body param names to values.
    :returns: (requests.Response) Returns response directly from requests.

    """
    url = build_url(RESOURCE)
    return request("post", url, json=body)


def retrieve(fid, share_key=None):
    """
    Retrieve a grid from Plotly.

    :param (str) fid: The `{username}:{idlocal}` identifier. E.g. `foo:88`.
    :param (str) share_key: The secret key granting 'read' access if private.
    :returns: (requests.Response) Returns response directly from requests.

    """
    url = build_url(RESOURCE, id=fid)
    params = make_params(share_key=share_key)
    return request("get", url, params=params)


def content(fid, share_key=None):
    """
    Retrieve full content for the grid (normal retrieve only yields preview)

    :param (str) fid: The `{username}:{idlocal}` identifier. E.g. `foo:88`.
    :param (str) share_key: The secret key granting 'read' access if private.
    :returns: (requests.Response) Returns response directly from requests.

    """
    url = build_url(RESOURCE, id=fid, route="content")
    params = make_params(share_key=share_key)
    return request("get", url, params=params)


def update(fid, body):
    """
    Update a grid from Plotly.

    :param (str) fid: The `{username}:{idlocal}` identifier. E.g. `foo:88`.
    :param (dict) body: A mapping of body param names to values.
    :returns: (requests.Response) Returns response directly from requests.

    """
    url = build_url(RESOURCE, id=fid)
    return request("put", url, json=body)


def trash(fid):
    """
    Soft-delete a grid from Plotly. (Can be undone with 'restore').

    :param (str) fid: The `{username}:{idlocal}` identifier. E.g. `foo:88`.
    :returns: (requests.Response) Returns response directly from requests.

    """
    url = build_url(RESOURCE, id=fid, route="trash")
    return request("post", url)


def restore(fid):
    """
    Restore a trashed grid from Plotly. See 'trash'.

    :param (str) fid: The `{username}:{idlocal}` identifier. E.g. `foo:88`.
    :returns: (requests.Response) Returns response directly from requests.

    """
    url = build_url(RESOURCE, id=fid, route="restore")
    return request("post", url)


def permanent_delete(fid):
    """
    Permanently delete a trashed grid file from Plotly. See 'trash'.

    :param (str) fid: The `{username}:{idlocal}` identifier. E.g. `foo:88`.
    :returns: (requests.Response) Returns response directly from requests.

    """
    url = build_url(RESOURCE, id=fid, route="permanent_delete")
    return request("delete", url)


def destroy(fid):
    """
    Permanently delete a grid file from Plotly.

    :param (str) fid: The `{username}:{idlocal}` identifier. E.g. `foo:88`.
    :returns: (requests.Response) Returns response directly from requests.

    """
    url = build_url(RESOURCE, id=fid)
    return request("delete", url)


def lookup(path, parent=None, user=None, exists=None):
    """
    Retrieve a grid file from Plotly without needing a fid.

    :param (str) path: The '/'-delimited path specifying the file location.
    :param (int) parent: Parent id, an integer, which the path is relative to.
    :param (str) user: The username to target files for. Defaults to requestor.
    :param (bool) exists: If True, don't return the full file, just a flag.
    :returns: (requests.Response) Returns response directly from requests.

    """
    url = build_url(RESOURCE, route="lookup")
    params = make_params(path=path, parent=parent, user=user, exists=exists)
    return request("get", url, params=params)


def col_create(fid, body):
    """
    Create a new column (or columns) inside a grid.

    :param (str) fid: The `{username}:{idlocal}` identifier. E.g. `foo:88`.
    :param (dict) body: A mapping of body param names to values.
    :returns: (requests.Response) Returns response directly from requests.

    """
    url = build_url(RESOURCE, id=fid, route="col")
    return request("post", url, json=body)


def col_retrieve(fid, uid):
    """
    Retrieve a column (or columns) from a grid.

    :param (str) fid: The `{username}:{idlocal}` identifier. E.g. `foo:88`.
    :param (str) uid: A ','-concatenated string of column uids in the grid.
    :returns: (requests.Response) Returns response directly from requests.

    """
    url = build_url(RESOURCE, id=fid, route="col")
    params = make_params(uid=uid)
    return request("get", url, params=params)


def col_update(fid, uid, body):
    """
    Update a column (or columns) from a grid.

    :param (str) fid: The `{username}:{idlocal}` identifier. E.g. `foo:88`.
    :param (str) uid: A ','-concatenated string of column uids in the grid.
    :param (dict) body: A mapping of body param names to values.
    :returns: (requests.Response) Returns response directly from requests.

    """
    url = build_url(RESOURCE, id=fid, route="col")
    params = make_params(uid=uid)
    return request("put", url, json=body, params=params)


def col_delete(fid, uid):
    """
    Permanently delete a column (or columns) from a grid.

    :param (str) fid: The `{username}:{idlocal}` identifier. E.g. `foo:88`.
    :param (str) uid: A ','-concatenated string of column uids in the grid.
    :returns: (requests.Response) Returns response directly from requests.

    """
    url = build_url(RESOURCE, id=fid, route="col")
    params = make_params(uid=uid)
    return request("delete", url, params=params)


def row(fid, body):
    """
    Append rows to a grid.

    :param (str) fid: The `{username}:{idlocal}` identifier. E.g. `foo:88`.
    :param (dict) body: A mapping of body param names to values.
    :returns: (requests.Response) Returns response directly from requests.

    """
    url = build_url(RESOURCE, id=fid, route="row")
    return request("post", url, json=body)
