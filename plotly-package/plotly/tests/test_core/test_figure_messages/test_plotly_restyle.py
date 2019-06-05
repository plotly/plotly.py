import sys
from unittest import TestCase

import plotly.graph_objs as go

if sys.version_info.major == 3 and sys.version_info.minor >= 3:
    from unittest.mock import MagicMock
else:
    from mock import MagicMock


class TestRestyleMessage(TestCase):

    def setUp(self):
        # Construct with mocked _send_restyle_msg method
        self.figure = go.Figure(data=[
            go.Scatter(),
            go.Bar(),
            go.Parcoords(dimensions=[{}, {'label': 'dim 2'}, {}])
        ])

        # Mock out the message method
        self.figure._send_restyle_msg = MagicMock()

    def test_property_assignment_toplevel(self):
        # Set bar marker
        self.figure.data[1].marker = {'color': 'green'}
        self.figure._send_restyle_msg.assert_called_once_with(
            {'marker': [{'color': 'green'}]}, trace_indexes=1)

    def test_property_assignment_nested(self):
        # Set scatter marker color
        self.figure.data[0].marker.color = 'green'
        self.figure._send_restyle_msg.assert_called_once_with(
            {'marker.color': ['green']}, trace_indexes=0)

    def test_property_assignment_nested_array(self):
        # Set parcoords dimension
        self.figure.data[2].dimensions[0].label = 'dim 1'
        self.figure._send_restyle_msg.assert_called_once_with(
            {'dimensions.0.label': ['dim 1']}, trace_indexes=2)

    # plotly_restyle
    def test_plotly_restyle_toplevel(self):
        # Set bar marker
        self.figure.plotly_restyle(
            {'marker': {'color': 'green'}}, trace_indexes=1)

        self.figure._send_restyle_msg.assert_called_once_with(
            {'marker': {'color': 'green'}}, trace_indexes=[1])

    def test_plotly_restyle_nested(self):
        # Set scatter marker color
        self.figure.plotly_restyle(
            {'marker.color': 'green'}, trace_indexes=0)

        self.figure._send_restyle_msg.assert_called_once_with(
            {'marker.color': 'green'}, trace_indexes=[0])

    def test_plotly_restyle_nested_array(self):
        # Set parcoords dimension
        self.figure.plotly_restyle(
            {'dimensions[0].label': 'dim 1'}, trace_indexes=2)

        self.figure._send_restyle_msg.assert_called_once_with(
            {'dimensions[0].label': 'dim 1'}, trace_indexes=[2])

    def test_plotly_restyle_multi_prop(self):
        self.figure.plotly_restyle(
            {'marker': {'color': 'green'},
             'name': 'MARKER 1'}, trace_indexes=1)

        self.figure._send_restyle_msg.assert_called_once_with(
            {'marker': {'color': 'green'},
             'name': 'MARKER 1'}, trace_indexes=[1])

    def test_plotly_restyle_multi_trace(self):
        self.figure.plotly_restyle(
            {'marker': {'color': 'green'},
             'name': 'MARKER 1'}, trace_indexes=[0, 1])

        self.figure._send_restyle_msg.assert_called_once_with(
            {'marker': {'color': 'green'},
             'name': 'MARKER 1'}, trace_indexes=[0, 1])
