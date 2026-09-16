from unittest import TestCase

import plotly.graph_objs as go
from plotly.basedatatypes import Undefined

from unittest.mock import MagicMock


class TestBatchUpdateMessage(TestCase):
    def setUp(self):
        # Construct initial scatter object
        self.figure = go.Figure(
            data=[
                go.Scatter(y=[3, 2, 1], marker={"color": "green"}),
                go.Bar(y=[3, 2, 1, 0, -1], marker={"opacity": 0.5}),
            ],
            layout={"xaxis": {"range": [-1, 4]}},
            frames=[go.Frame(layout={"yaxis": {"title": "f1"}})],
        )

        # Mock out the message method
        self.figure._send_update_msg = MagicMock()

    def test_batch_update(self):
        with self.figure.batch_update():
            # Assign trace property
            self.figure.data[0].marker.color = "yellow"
            self.figure.data[1].marker.opacity = 0.9

            # Assign layout property
            self.figure.layout.xaxis.range = [10, 20]

            # Assign frame property
            self.figure.frames[0].layout.yaxis.title.text = "f2"

            # Make sure that trace/layout assignments haven't been applied yet
            self.assertEqual(self.figure.data[0].marker.color, "green")
            self.assertEqual(self.figure.data[1].marker.opacity, 0.5)
            self.assertEqual(self.figure.layout.xaxis.range, (-1, 4))

            # Expect the frame update to be applied immediately
            self.assertEqual(self.figure.frames[0].layout.yaxis.title.text, "f2")

        # Make sure that trace/layout assignments have been applied after
        # context exits
        self.assertEqual(self.figure.data[0].marker.color, "yellow")
        self.assertEqual(self.figure.data[1].marker.opacity, 0.9)
        self.assertEqual(self.figure.layout.xaxis.range, (10, 20))

        # Check that update message was sent
        self.figure._send_update_msg.assert_called_once_with(
            restyle_data={
                "marker.color": ["yellow", Undefined],
                "marker.opacity": [Undefined, 0.9],
            },
            relayout_data={"xaxis.range": [10, 20]},
            trace_indexes=[0, 1],
        )

    def test_add_layout_objects_in_batch_update(self):
        self.figure._send_relayout_msg = MagicMock()

        with self.figure.batch_update():
            self.figure.add_shape(type="line", x0=0, x1=1, y0=0, y1=1)
            self.figure.add_shape(type="rect", x0=1, x1=2, y0=1, y1=2)
            self.figure.add_annotation(text="a", x=0, y=0)
            self.figure.layout.xaxis.range = [10, 20]

            # Like traces, layout objects are added right away
            self.assertEqual(
                [s.type for s in self.figure.layout.shapes], ["line", "rect"]
            )
            self.assertEqual(self.figure.layout.annotations[0].text, "a")
            self.assertEqual(self.figure._send_relayout_msg.call_count, 3)

            # while property assignments still wait for the context to exit
            self.assertEqual(self.figure.layout.xaxis.range, (-1, 4))

        self.assertEqual(self.figure.layout.xaxis.range, (10, 20))
        self.figure._send_update_msg.assert_called_once()
        self.assertEqual(
            self.figure._send_update_msg.call_args.kwargs["relayout_data"],
            {"xaxis.range": [10, 20]},
        )

    def test_plotly_update(self):
        self.figure.plotly_update(
            restyle_data={
                "marker.color": ["yellow", Undefined],
                "marker.opacity": [Undefined, 0.9],
            },
            relayout_data={"xaxis.range": [10, 20]},
            trace_indexes=[0, 1],
        )

        # Make sure that trace/layout assignments have been applied after
        # context exits
        self.assertEqual(self.figure.data[0].marker.color, "yellow")
        self.assertEqual(self.figure.data[1].marker.opacity, 0.9)
        self.assertEqual(self.figure.layout.xaxis.range, (10, 20))

        # Check that update message was sent
        self.figure._send_update_msg.assert_called_once_with(
            restyle_data={
                "marker.color": ["yellow", Undefined],
                "marker.opacity": [Undefined, 0.9],
            },
            relayout_data={"xaxis.range": [10, 20]},
            trace_indexes=[0, 1],
        )
