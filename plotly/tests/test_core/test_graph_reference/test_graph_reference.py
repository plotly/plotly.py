"""
A module to test functionality related to *using* the graph reference.

"""
from __future__ import absolute_import

from unittest import TestCase

from plotly.graph_reference import object_name_to_class_name


class TestObjectNameToClass(TestCase):

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
