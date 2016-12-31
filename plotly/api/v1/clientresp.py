"""Interface to deprecated /clientresp API. Subject to deletion."""
from __future__ import absolute_import

import warnings

from requests.compat import json as _json

from plotly import config, utils, version
from plotly.api.v1.utils import request


def clientresp(data, **kwargs):
    """
    Deprecated endpoint, still used because it can parse data out of a plot.

    When we get around to forcing users to create grids and then create plots,
    we can finally get rid of this.

    :param (list) data: The data array from a figure.

    """
    creds = config.get_credentials()
    cfg = config.get_config()

    dumps_kwargs = {'sort_keys': True, 'cls': utils.PlotlyJSONEncoder}

    payload = {
        'platform': 'python', 'version': version.__version__,
        'args': _json.dumps(data, **dumps_kwargs),
        'un': creds['username'], 'key': creds['api_key'], 'origin': 'plot',
        'kwargs': _json.dumps(kwargs, **dumps_kwargs)
    }

    url = '{plotly_domain}/clientresp'.format(**cfg)
    response = request('post', url, data=payload)

    # Old functionality, just keeping it around.
    parsed_content = response.json()
    if parsed_content.get('warning'):
        warnings.warn(parsed_content['warning'])
    if parsed_content.get('message'):
        print(parsed_content['message'])

    return response
