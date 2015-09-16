"""
A module to test functionality related to *using* the graph reference.

"""
from __future__ import absolute_import

from plotly import exceptions, files, graph_reference as gr, tools, utils
from plotly.tests.utils import PlotlyTestCase


class TestGraphReferenceCaching(PlotlyTestCase):

    def set_graph_reference(self, graph_reference):
        if files.check_file_permissions():
            utils.save_json_dict(files.GRAPH_REFERENCE_FILE, graph_reference)

    def test_get_graph_reference_outdated(self):

        # if the hash of the current graph reference doesn't match the hash of
        # the graph reference a Plotly server has, we should update!

        outdated_graph_reference = {'real': 'old'}
        self.set_graph_reference(outdated_graph_reference)
        graph_reference = gr.get_graph_reference()
        self.assertNotEqual(graph_reference, outdated_graph_reference)

    def test_get_graph_reference_bad_request_local_copy(self):

        # if the request fails (mocked by using a bad url here) and a local
        # copy of the graph reference exists, we can just use that.

        tools.set_config_file(plotly_api_domain='api.am.not.here.ly')
        local_graph_reference = {'real': 'local'}
        self.set_graph_reference(local_graph_reference)
        graph_reference = gr.get_graph_reference()
        self.assertEqual(graph_reference, local_graph_reference)

    def test_get_graph_reference_bad_request_no_copy(self):

        # if we don't have a graph reference we *have* to error, no choice :(

        tools.set_config_file(plotly_api_domain='api.am.not.here.ly')
        empty_graph_reference = {}  # set it to a false-y value.
        self.set_graph_reference(empty_graph_reference)
        with self.assertRaisesRegexp(exceptions.PlotlyError, 'schema'):
            gr.get_graph_reference()
