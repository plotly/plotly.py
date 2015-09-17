"""
A module to test functionality related to *using* the graph reference.

"""
from __future__ import absolute_import

import json
import os
from pkg_resources import resource_string

from nose.plugins.attrib import attr

from plotly import files, graph_reference as gr, tools, utils
from plotly.graph_reference import object_name_to_class_name
from plotly.tests.utils import PlotlyTestCase


class TestGraphReferenceCaching(PlotlyTestCase):

    def set_graph_reference(self, graph_reference):
        if files.check_file_permissions():
            utils.save_json_dict(files.GRAPH_REFERENCE_FILE, graph_reference)

    @attr('slow')
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

        # if we don't have a graph reference we load an outdated default

        tools.set_config_file(plotly_api_domain='api.am.not.here.ly')
        empty_graph_reference = {}  # set it to a false-y value.
        self.set_graph_reference(empty_graph_reference)
        path = os.path.join('graph_reference', 'default-schema.json')
        s = resource_string('plotly', path).decode('utf-8')
        default_graph_reference = json.loads(s)
        graph_reference = gr.get_graph_reference()
        self.assertEqual(graph_reference, default_graph_reference)


class TestObjectNameToClass(PlotlyTestCase):

    def test_capitalize_first_letter(self):

        object_names = ['marker', 'line', 'scatter']
        class_names = ['Marker', 'Line', 'Scatter']
        for object_name, class_name in zip(object_names, class_names):
            self.assertEqual(
                object_name_to_class_name(object_name), class_name
            )

    def test_capitalize_after_underscore(self):

        object_names = ['error_y', 'error_x']
        class_names = ['ErrorY', 'ErrorX']
        for object_name, class_name in zip(object_names, class_names):
            self.assertEqual(
                object_name_to_class_name(object_name), class_name
            )

    def test_use_hr_name(self):

        # we should be checking for an hr_name in the plot schema.

        object_name = 'histogram2dcontour'
        class_name = 'Histogram2DContour'
        self.assertEqual(object_name_to_class_name(object_name), class_name)
