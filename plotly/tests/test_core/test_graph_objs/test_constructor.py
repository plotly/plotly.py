from unittest import TestCase
import plotly.graph_objs as go
from nose.tools import raises


class TestGraphObjConstructor(TestCase):

    def test_kwarg(self):
        m = go.scatter.Marker(color='green')
        self.assertEqual(m.to_plotly_json(),
                         {'color': 'green'})

    def test_valid_arg_dict(self):
        m = go.scatter.Marker(dict(color='green'))
        self.assertEqual(m.to_plotly_json(),
                         {'color': 'green'})

    def test_valid_arg_obj(self):
        m = go.scatter.Marker(
            go.scatter.Marker(color='green'))

        self.assertEqual(m.to_plotly_json(),
                         {'color': 'green'})

    def test_kwarg_takes_precedence(self):
        m = go.scatter.Marker(
            dict(color='green',
                 size=12),
            color='blue',
            opacity=0.6
        )

        self.assertEqual(m.to_plotly_json(),
                         {'color': 'blue',
                          'size': 12,
                          'opacity': 0.6})

    @raises(ValueError)
    def test_invalid_kwarg(self):
        go.scatter.Marker(bogus=[1, 2, 3])

    @raises(ValueError)
    def test_invalid_arg(self):
        go.scatter.Marker([1, 2, 3])

    @raises(ValueError)
    def test_valid_arg_with_invalid_key_name(self):
        go.scatter.Marker({'bogus': 12})

    @raises(ValueError)
    def test_valid_arg_with_invalid_key_value(self):
        go.scatter.Marker({'color': 'bogus'})
