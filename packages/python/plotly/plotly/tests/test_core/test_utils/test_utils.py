from __future__ import absolute_import

from unittest import TestCase

import json as _json

from plotly.utils import PlotlyJSONEncoder, get_by_path, node_generator
from time import time
import numpy as np
import plotly.graph_objects as go


class TestJSONEncoder(TestCase):
    def test_nan_to_null(self):
        array = [1, float("NaN"), float("Inf"), float("-Inf"), "platypus"]
        result = _json.dumps(array, cls=PlotlyJSONEncoder)
        expected_result = '[1, null, null, null, "platypus"]'
        self.assertEqual(result, expected_result)

    def test_invalid_encode_exception(self):
        with self.assertRaises(TypeError):
            _json.dumps({"a": {1}}, cls=PlotlyJSONEncoder)

    def test_fast_track_finite_arrays(self):
        # if NaN or Infinity is found in the json dump
        # of a figure, it is decoded and re-encoded to replace these values
        # with null. This test checks that NaN and Infinity values are
        # indeed converted to null, and that the encoding of figures
        # without inf or nan is faster (because we can avoid decoding
        # and reencoding).
        z = np.random.randn(100, 100)
        x = np.arange(100.0)
        fig_1 = go.Figure(go.Heatmap(z=z, x=x))
        t1 = time()
        json_str_1 = _json.dumps(fig_1, cls=PlotlyJSONEncoder)
        t2 = time()
        x[0] = np.nan
        x[1] = np.inf
        fig_2 = go.Figure(go.Heatmap(z=z, x=x))
        t3 = time()
        json_str_2 = _json.dumps(fig_2, cls=PlotlyJSONEncoder)
        t4 = time()
        assert t2 - t1 < t4 - t3
        assert "null" in json_str_2
        assert "NaN" not in json_str_2
        assert "Infinity" not in json_str_2
        x = np.arange(100.0)
        fig_3 = go.Figure(go.Heatmap(z=z, x=x))
        fig_3.update_layout(title_text="Infinity")
        t5 = time()
        json_str_3 = _json.dumps(fig_3, cls=PlotlyJSONEncoder)
        t6 = time()
        assert t2 - t1 < t6 - t5
        assert "Infinity" in json_str_3


class TestGetByPath(TestCase):
    def test_get_by_path(self):

        # should be able to traverse into a nested dict/list with key array

        figure = {"data": [{}, {"marker": {"color": ["red", "blue"]}}]}
        path = ("data", 1, "marker", "color")
        value = get_by_path(figure, path)
        expected_value = ["red", "blue"]
        self.assertEqual(value, expected_value)


class TestNodeGenerator(TestCase):
    def test_node_generator(self):

        # should generate a (node, path) pair for each dict in a dict

        node4 = {"h": 5}
        node3 = {"g": 7}
        node2 = {"e": node3}
        node1 = {"c": node2, "d": ["blah"]}
        node0 = {"a": node1, "b": 8}

        expected_node_path_tuples = [
            (node0, ()),
            (node1, ("a",)),
            (node2, ("a", "c")),
            (node3, ("a", "c", "e")),
            (node4, ("a", "c", "f")),
        ]
        for i, item in enumerate(node_generator(node0)):
            self.assertEqual(item, expected_node_path_tuples[i])


class TestNumpyIntegerBaseType(TestCase):
    def test_numpy_integer_import(self):
        # should generate a figure with subplots of array and not throw a ValueError
        import numpy as np
        import plotly.graph_objects as go
        from plotly.subplots import make_subplots

        indices_rows = np.array([1], dtype=np.int)
        indices_cols = np.array([1], dtype=np.int)
        fig = make_subplots(rows=1, cols=1)
        fig.add_trace(go.Scatter(y=[1]), row=indices_rows[0], col=indices_cols[0])

        data_path = ("data", 0, "y")
        value = get_by_path(fig, data_path)
        expected_value = (1,)
        self.assertEqual(value, expected_value)

    def test_get_numpy_int_type(self):
        import numpy as np
        from _plotly_utils.utils import _get_int_type

        int_type_tuple = _get_int_type()
        expected_tuple = (int, np.integer)

        self.assertEqual(int_type_tuple, expected_tuple)


class TestNoNumpyIntegerBaseType(TestCase):
    def test_no_numpy_int_type(self):
        import sys
        from _plotly_utils.utils import _get_int_type
        from _plotly_utils.optional_imports import get_module

        np = get_module("numpy", should_load=False)
        if np:
            sys.modules.pop("numpy")

        int_type_tuple = _get_int_type()
        expected_tuple = (int,)

        self.assertEqual(int_type_tuple, expected_tuple)
