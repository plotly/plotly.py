from __future__ import absolute_import

from unittest import TestCase

from plotly.graph_objs import graph_objs as go
from plotly.graph_objs import graph_objs_tools as got


class TestGetRole(TestCase):

    def test_get_role_no_value(self):

        # this is a bit fragile, but we pick a few stable values

        # the location in the figure matters for this test!
        fig = go.Figure(data=[{}])
        fig.data[0].marker.color = 'red'
        fig.layout.title = 'some-title'

        parent_key_role_tuples = [
            (fig.data[0], 'x', 'data'),
            (fig.data[0], 'marker', 'object'),
            (fig.data[0].marker, 'color', 'style'),
            (fig.layout, 'title', 'info'),
            (fig, 'data', 'object'),
        ]
        for parent, key, role in parent_key_role_tuples:
            self.assertEqual(got.get_role(parent, key), role, msg=key)

    def test_get_role_with_value(self):

        # some attributes are conditionally considered data if they're arrays

        # the location in the figure matters for this test!
        fig = go.Figure(data=[{}])
        fig.data[0].marker.color = 'red'

        parent_key_value_role_tuples = [
            (fig.data[0], 'x', 'wh0cares', 'data'),
            (fig.data[0], 'marker', 'wh0cares', 'object'),
            (fig.data[0].marker, 'color', 'red', 'style'),
            (fig.data[0].marker, 'color', ['red'], 'data')
        ]
        for parent, key, value, role in parent_key_value_role_tuples:
            self.assertEqual(got.get_role(parent, key, value), role,
                             msg=(key, value))
