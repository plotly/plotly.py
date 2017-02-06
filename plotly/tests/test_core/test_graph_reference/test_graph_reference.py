"""
A module to test functionality related to *using* the graph reference.

"""
from __future__ import absolute_import

import os
from pkg_resources import resource_string
from unittest import TestCase

from nose.plugins.attrib import attr
from requests.compat import json as _json

from plotly import graph_reference as gr
from plotly.api import v2
from plotly.graph_reference import string_to_class_name, get_role
from plotly.tests.utils import PlotlyTestCase

FAKE_API_DOMAIN = 'https://api.am.not.here.ly'


class TestGraphReferenceCaching(PlotlyTestCase):

    @attr('slow')
    def test_default_schema_is_up_to_date(self):
        response = v2.plot_schema.retrieve('')
        schema = response.json()['schema']

        path = os.path.join('package_data', 'default-schema.json')
        s = resource_string('plotly', path).decode('utf-8')
        default_schema = _json.loads(s)

        msg = (
            'The default, hard-coded plot schema we ship with pip is out of '
            'sync with the prod plot schema!\n'
            'Run `make update_default_schema` to fix it!'
        )
        self.assertEqual(schema, default_schema, msg=msg)


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


class TestObjectNameToClassName(TestCase):

    def test_backwards_compat(self):

        # Old classes should still be shown to users.

        test_tuples = [
            ('angularaxis', 'AngularAxis'),
            ('annotation', 'Annotation'),
            ('annotations', 'Annotations'),
            ('area', 'Area'),
            ('colorbar', 'ColorBar'),
            ('contour', 'Contour'),
            ('contours', 'Contours'),
            ('data', 'Data'),
            ('error_x', 'ErrorX'),
            ('error_y', 'ErrorY'),
            ('error_z', 'ErrorZ'),
            ('figure', 'Figure'),
            ('font', 'Font'),
            ('layout', 'Layout'),
            ('legend', 'Legend'),
            ('margin', 'Margin'),
            ('marker', 'Marker'),
            ('radialaxis', 'RadialAxis'),
            ('scene', 'Scene'),
            ('stream', 'Stream'),
            ('xaxis', 'XAxis'),
            ('xbins', 'XBins'),
            ('yaxis', 'YAxis'),
            ('ybins', 'YBins'),
            ('zaxis', 'ZAxis')
        ]

        for object_name, expected_class_name in test_tuples:
            class_name = gr.object_name_to_class_name(object_name)
            msg = (object_name, expected_class_name, class_name)
            self.assertEqual(class_name, expected_class_name, msg=msg)

    def test_old_traces(self):

        # While the old trace classes exist, the newer should be returned.

        test_tuples = [
            ('histogram2dcontour', 'Histogram2dcontour')
        ]

        for object_name, expected_class_name in test_tuples:
            class_name = gr.object_name_to_class_name(object_name)
            msg = (object_name, expected_class_name, class_name)
            self.assertEqual(class_name, expected_class_name, msg=msg)

    def test_new_traces(self):

        # New traces should get have classes defined.

        test_tuples = [
            ('choropleth', 'Choropleth'),
            ('pie', 'Pie')
        ]

        for object_name, expected_class_name in test_tuples:
            class_name = gr.object_name_to_class_name(object_name)
            msg = (object_name, expected_class_name, class_name)
            self.assertEqual(class_name, expected_class_name, msg=msg)

    def test_new_non_trace_objects(self):

        # New objects get 'dict' or 'list'.

        test_tuples = [
            ('geo', 'dict'),
            ('shapes', 'list'),
            ('shape', 'dict'),
        ]

        for object_name, expected_class_name in test_tuples:
            class_name = gr.object_name_to_class_name(object_name)
            msg = (object_name, expected_class_name, class_name)
            self.assertEqual(class_name, expected_class_name, msg=msg)


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
