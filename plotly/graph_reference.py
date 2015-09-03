"""
This module handles accessing, storing, and managing the graph reference.

"""
from __future__ import absolute_import

import json
import requests

from plotly import exceptions, files, utils

GRAPH_REFERENCE_PATH = '/plot-schema.json'

def get_graph_reference():
    """
    Attempts to load local copy of graph reference or makes GET request if DNE.

    :return: (dict) The graph reference.
    :raises: (PlotlyError) When graph reference DNE and GET request fails.

    """
    if files.check_file_permissions():
        graph_reference = utils.load_json_dict(files.GRAPH_REFERENCE_FILE)
        config = utils.load_json_dict(files.CONFIG_FILE)
        plotly_domain = config['plotly_domain']
    else:
        graph_reference = {}
        plotly_domain = files.FILE_CONTENT[files.CONFIG_FILE]['plotly_domain']

    if not graph_reference:

        graph_reference_url = plotly_domain + GRAPH_REFERENCE_PATH

        try:
            response = requests.get(graph_reference_url)
            response.raise_for_status()
        except requests.exceptions.RequestException:
            raise exceptions.PlotlyError(
                "The schema used to validate Plotly figures has never been "
                "downloaded to your computer. You'll need to connect to a "
                "Plotly server at least once to do this.\n"
                "You're seeing this error because the attempt to download "
                "the schema from '{}' failed.".format(graph_reference_url)
            )

        # TODO: Hash this so we don't have to load it every time. The server
        #       will need to accept a hash query param as well.
        graph_reference = json.loads(response.content)

    return utils.decode_unicode(graph_reference)

GRAPH_REFERENCE = get_graph_reference()
