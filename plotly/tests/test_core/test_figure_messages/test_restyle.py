from unittest import TestCase
from mock import MagicMock
import plotly.graph_objs as go


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
