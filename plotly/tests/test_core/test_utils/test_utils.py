from __future__ import absolute_import

import json
from unittest import TestCase

from plotly.utils import PlotlyJSONEncoder, get_by_path, node_generator


class TestJSONEncoder(TestCase):

    def test_nan_to_null(self):
        array = [1, float('NaN'), float('Inf'), float('-Inf'), 'platypus']
        result = json.dumps(array, cls=PlotlyJSONEncoder)
        expected_result = '[1, null, null, null, "platypus"]'
        self.assertEqual(result, expected_result)


class TestGetByPath(TestCase):

    def test_get_by_path(self):

        # should be able to traverse into a nested dict/list with key array

        figure = {'data': [{}, {'marker': {'color': ['red', 'blue']}}]}
        path = ('data', 1, 'marker', 'color')
        value = get_by_path(figure, path)
        expected_value = ['red', 'blue']
        self.assertEqual(value, expected_value)


class TestNodeGenerator(TestCase):

    def test_node_generator(self):

        # should generate a (node, path) pair for each dict in a dict

        node4 = {'h': 5}
        node3 = {'g': 7}
        node2 = {'e': node3}
        node1 = {'c': node2, 'd': ['blah']}
        node0 = {'a': node1, 'b': 8}

        expected_node_path_tuples = [
            (node0, ()),
            (node1, ('a',)),
            (node2, ('a', 'c')),
            (node3, ('a', 'c', 'e')),
            (node4, ('a', 'c', 'f'))
        ]
        for i, item in enumerate(node_generator(node0)):
            self.assertEqual(item, expected_node_path_tuples[i])
