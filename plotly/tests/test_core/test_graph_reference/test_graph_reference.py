"""
A module to test functionality related to *using* the graph reference.

"""
from __future__ import absolute_import

import json
import os
from pkg_resources import resource_string
from unittest import TestCase

from nose.plugins.attrib import attr

from plotly import files, graph_reference as gr, tools, utils
from plotly.graph_reference import string_to_class_name, get_role
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


class TestStringToClass(PlotlyTestCase):

    def test_capitalize_first_letter(self):

        object_names = ['marker', 'line', 'scatter']
        class_names = ['Marker', 'Line', 'Scatter']
        for object_name, class_name in zip(object_names, class_names):
            self.assertEqual(string_to_class_name(object_name), class_name)

    def test_capitalize_after_underscore(self):

        object_names = ['error_y', 'error_x']
        class_names = ['ErrorY', 'ErrorX']
        for object_name, class_name in zip(object_names, class_names):
            self.assertEqual(string_to_class_name(object_name), class_name)


class TestGetAttributesMethods(TestCase):

    def test_get_subplot_attributes(self):

        # importantly, layout should have a bunch of these

        layout_subplot_attributes = gr.get_subplot_attributes('layout')

        # there may be more...
        expected_attributes = ['xaxis', 'yaxis', 'geo', 'scene']

        for expected_attribute in expected_attributes:
            self.assertIn(expected_attribute, layout_subplot_attributes)

    def test_get_deprecated_attributes(self):

        # this may eventually break, but it's important to check *something*

        bar_deprecated_attributes = gr.get_deprecated_attributes('bar')

        expected_attributes = ['bardir']

        for expected_attribute in expected_attributes:
            self.assertIn(expected_attribute, bar_deprecated_attributes)


class TestGetAttributePathToObjectNames(TestCase):

    def test_layout_attributes(self):

        # layout attrs defined under traces should still show up under layout

        graph_reference_path = ('traces', 'box', 'layoutAttributes')
        expected_object_names = ('figure', 'layout')
        object_names = gr.attribute_path_to_object_names(graph_reference_path)
        self.assertEqual(object_names, expected_object_names)

    def test_trace_attributes(self):

        # trace attributes should be found under 'data' somewhere

        graph_reference_path = ('traces', 'scatter', 'attributes', 'marker',
                                'line')
        expected_object_names = ('figure', 'data', 'scatter', 'marker', 'line')
        object_names = gr.attribute_path_to_object_names(graph_reference_path)
        self.assertEqual(object_names, expected_object_names)


class TestGetRole(TestCase):

    def test_get_role_no_value(self):

        # this is a bit fragile, but we pick a few stable values

        # (<object_name>, <attribute_name>, <parent_object_names>, <role>)
        test_tuples = [
            ('scatter', 'x', ('figure', 'data'), 'data'),
            ('scatter', 'marker', ('figure', 'data'), 'object'),
            ('marker', 'color', ('figure', 'data', 'scatter'), 'style'),
            ('layout', 'title', ('figure', ), 'info'),
            ('figure', 'data', (), 'object')
        ]

        for tup in test_tuples:
            object_name, key, parent_object_names, role = tup
            found_role = get_role(object_name, key,
                                  parent_object_names=parent_object_names)
            self.assertEqual(found_role, role, msg=tup)

    def test_get_role_with_value(self):

        # some attributes are conditionally considered data if they're arrays

        # (<object_name>, <attribute_name>, <parent_object_names>, <role>)
        test_tuples = [
            ('scatter', 'x', 'wh0cares', ('figure', 'data'), 'data'),
            ('scatter', 'marker', 'wh0cares', ('figure', 'data'), 'object'),
            ('marker', 'color', 'r', ('figure', 'data', 'scatter'), 'style'),
            ('marker', 'color', ['r'], ('figure', 'data', 'scatter'), 'data'),
        ]

        for tup in test_tuples:
            object_name, key, value, parent_object_names, role = tup
            found_role = get_role(object_name, key, value=value,
                                  parent_object_names=parent_object_names)
            self.assertEqual(found_role, role, msg=tup)
