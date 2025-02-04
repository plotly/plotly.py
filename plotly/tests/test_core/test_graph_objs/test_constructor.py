from unittest import TestCase
import plotly.graph_objs as go
import pytest


class TestGraphObjConstructor(TestCase):
    def test_kwarg(self):
        m = go.scatter.Marker(color="green")
        self.assertEqual(m.to_plotly_json(), {"color": "green"})

    def test_valid_arg_dict(self):
        m = go.scatter.Marker(dict(color="green"))
        self.assertEqual(m.to_plotly_json(), {"color": "green"})

    def test_valid_underscore_kwarg(self):
        m = go.scatter.Marker(line_color="green")
        self.assertEqual(m.to_plotly_json(), {"line": {"color": "green"}})

    def test_valid_arg_obj(self):
        m = go.scatter.Marker(go.scatter.Marker(color="green"))

        self.assertEqual(m.to_plotly_json(), {"color": "green"})

    def test_kwarg_takes_precedence(self):
        m = go.scatter.Marker(dict(color="green", size=12), color="blue", opacity=0.6)

        self.assertEqual(
            m.to_plotly_json(), {"color": "blue", "size": 12, "opacity": 0.6}
        )

    def test_invalid_kwarg(self):
        with pytest.raises(ValueError):
            go.scatter.Marker(bogus=[1, 2, 3])

    def test_invalid_arg(self):
        with pytest.raises(ValueError):
            go.scatter.Marker([1, 2, 3])

    def test_valid_arg_with_invalid_key_name(self):
        with pytest.raises(ValueError):
            go.scatter.Marker({"bogus": 12})

    def test_valid_arg_with_invalid_key_value(self):
        with pytest.raises(ValueError):
            go.scatter.Marker({"color": "bogus"})
