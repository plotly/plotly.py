from __future__ import absolute_import

from unittest import TestCase

from plotly.graph_objs.graph_objs_tools import value_is_data


class TestValueIsData(TestCase):

    def test_unknown_strings(self):
        self.assertFalse(value_is_data('scatter', 'blah', ''))
        self.assertFalse(value_is_data('huh?', 'text', None))

    def test_data_value_type(self):
        self.assertTrue(value_is_data('scatter', 'x', {}))
        self.assertTrue(value_is_data('bar', 'name', 'bill'))
        self.assertTrue(value_is_data('histogram', 'x', [5, 5]))
        self.assertTrue(value_is_data('xaxis', 'range', [0, 5]))

    def test_style_value_type(self):
        self.assertFalse(value_is_data('marker', 'color', 'red'))
        self.assertTrue(value_is_data('marker', 'color', ['red', 'blue']))
        self.assertTrue(value_is_data('marker', 'opacity', (.9, .5)))
        self.assertFalse(value_is_data('marker', 'symbol', {}))
