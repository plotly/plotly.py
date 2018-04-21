from unittest import TestCase
from mock import MagicMock
import plotly.graph_objs as go
from plotly.basedatatypes import Undefined


class TestBatchUpdate(TestCase):
    def setUp(self):
        # Construct initial scatter object
        self.figure = go.Figure(data=[
            go.Scatter(y=[3, 2, 1], marker={'color': 'green'}),
            go.Bar(y=[3, 2, 1, 0, -1], marker={'opacity': 0.5})],
                                layout={'xaxis': {'range': [-1, 4]}},
                                frames=[go.Frame(
                                    layout={'yaxis':
                                            {'title': 'f1'}})])

        # Mock out the _send_update_msg method
        self.figure._send_update_msg = MagicMock()

    def test_batch_update(self):

        with self.figure.batch_update():

            # Assign trace property
            self.figure.data[0].marker.color = 'yellow'
            self.figure.data[1].marker.opacity = 0.9

            # Assign layout property
            self.figure.layout.xaxis.range = [10, 20]

            # Assign frame property
            self.figure.frames[0].layout.yaxis.title = 'f2'

            # Make sure that trace/layout assignments haven't been applied yet
            self.assertEqual(self.figure.data[0].marker.color, 'green')
            self.assertEqual(self.figure.data[1].marker.opacity, 0.5)
            self.assertEqual(self.figure.layout.xaxis.range, (-1, 4))

            # Expect the frame update to be applied immediately
            self.assertEqual(self.figure.frames[0].layout.yaxis.title, 'f2')

        # Make sure that trace/layout assignments have been applied after
        # context exits
        self.assertEqual(self.figure.data[0].marker.color, 'yellow')
        self.assertEqual(self.figure.data[1].marker.opacity, 0.9)
        self.assertEqual(self.figure.layout.xaxis.range, (10, 20))

        # Check that update message was sent
        self.figure._send_update_msg.assert_called_once_with(
            style={'marker.color': ['yellow', Undefined],
                   'marker.opacity': [Undefined, 0.9]},
            layout={'xaxis.range': [10, 20]},
            trace_indexes=[0, 1])
