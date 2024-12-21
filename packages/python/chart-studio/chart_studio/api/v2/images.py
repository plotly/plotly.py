"""Interface to Plotly's /v2/images endpoints."""


from chart_studio.api.v2.utils import build_url, request

RESOURCE = "images"


def create(body):
    """
    Generate an image (which does not get saved on Plotly).

    :param (dict) body: A mapping of body param names to values.
    :returns: (requests.Response) Returns response directly from requests.

    """
    url = build_url(RESOURCE)
    return request("post", url, json=body)
