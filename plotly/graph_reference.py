"""
This module handles accessing, storing, and managing the graph reference.

"""
from __future__ import absolute_import

import hashlib
import json
import os
import requests
from pkg_resources import resource_string

import six

from plotly import exceptions, files, utils

GRAPH_REFERENCE_PATH = '/v2/plot-schema'


def get_graph_reference():
    """
    Attempts to load local copy of graph reference or makes GET request if DNE.

    :return: (dict) The graph reference.
    :raises: (PlotlyError) When graph reference DNE and GET request fails.

    """
    default_config = files.FILE_CONTENT[files.CONFIG_FILE]
    if files.check_file_permissions():
        graph_reference = utils.load_json_dict(files.GRAPH_REFERENCE_FILE)
        config = utils.load_json_dict(files.CONFIG_FILE)

        # TODO: https://github.com/plotly/python-api/issues/293
        plotly_api_domain = config.get('plotly_api_domain',
                                       default_config['plotly_api_domain'])
    else:
        graph_reference = {}
        plotly_api_domain = default_config['plotly_api_domain']

    sha1 = hashlib.sha1(six.b(str(graph_reference))).hexdigest()

    graph_reference_url = '{}{}?sha1={}'.format(plotly_api_domain,
                                                GRAPH_REFERENCE_PATH, sha1)

    try:
        response = requests.get(graph_reference_url)
        response.raise_for_status()
    except requests.exceptions.RequestException:
        if not graph_reference:
            path = os.path.join('graph_reference', 'default-schema.json')
            s = resource_string('plotly', path).decode('utf-8')
            graph_reference = json.loads(s)
    else:
        if six.PY3:
            content = str(response.content, encoding='utf-8')
        else:
            content = response.content
        data = json.loads(content)
        if data['modified']:
            graph_reference = data['schema']

    return utils.decode_unicode(graph_reference)

GRAPH_REFERENCE = get_graph_reference()
