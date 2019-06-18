"""Interface to Plotly's /v2/files endpoints."""
from __future__ import absolute_import

from chart_studio.api.v2.utils import build_url, make_params, request

RESOURCE = "files"


def retrieve(fid, share_key=None):
    """
    Retrieve a general file from Plotly.

    :param (str) fid: The `{username}:{idlocal}` identifier. E.g. `foo:88`.
    :param (str) share_key: The secret key granting 'read' access if private.
    :returns: (requests.Response) Returns response directly from requests.

    """
    url = build_url(RESOURCE, id=fid)
    params = make_params(share_key=share_key)
    return request("get", url, params=params)


def update(fid, body):
    """
    Update a general file from Plotly.

    :param (str) fid: The `{username}:{idlocal}` identifier. E.g. `foo:88`.
    :param (dict) body: A mapping of body param names to values.
    :returns: (requests.Response) Returns response directly from requests.

    """
    url = build_url(RESOURCE, id=fid)
    return request("put", url, json=body)


def trash(fid):
    """
    Soft-delete a general file from Plotly. (Can be undone with 'restore').

    :param (str) fid: The `{username}:{idlocal}` identifier. E.g. `foo:88`.
    :returns: (requests.Response) Returns response directly from requests.

    """
    url = build_url(RESOURCE, id=fid, route="trash")
    return request("post", url)


def restore(fid):
    """
    Restore a trashed, general file from Plotly. See 'trash'.

    :param (str) fid: The `{username}:{idlocal}` identifier. E.g. `foo:88`.
    :returns: (requests.Response) Returns response directly from requests.

    """
    url = build_url(RESOURCE, id=fid, route="restore")
    return request("post", url)


def permanent_delete(fid):
    """
    Permanently delete a trashed, general file from Plotly. See 'trash'.

    :param (str) fid: The `{username}:{idlocal}` identifier. E.g. `foo:88`.
    :returns: (requests.Response) Returns response directly from requests.

    """
    url = build_url(RESOURCE, id=fid, route="permanent_delete")
    return request("delete", url)


def lookup(path, parent=None, user=None, exists=None):
    """
    Retrieve a general file from Plotly without needing a fid.

    :param (str) path: The '/'-delimited path specifying the file location.
    :param (int) parent: Parent id, an integer, which the path is relative to.
    :param (str) user: The username to target files for. Defaults to requestor.
    :param (bool) exists: If True, don't return the full file, just a flag.
    :returns: (requests.Response) Returns response directly from requests.

    """
    url = build_url(RESOURCE, route="lookup")
    params = make_params(path=path, parent=parent, user=user, exists=exists)
    return request("get", url, params=params)
