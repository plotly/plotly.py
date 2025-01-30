import sys
from unittest import TestCase

import plotly.graph_objs as go
from plotly.subplots import make_subplots

if sys.version_info >= (3, 3):
    from unittest.mock import MagicMock
else:
    from mock import MagicMock


class TestAddTracesMessage(TestCase):
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
        self.figure._send_addTraces_msg = MagicMock()

    def test_add_trace(self):
        # Add a trace
        self.figure.add_trace(go.Sankey(arrangement="snap"))

        # Check access properties
        self.assertEqual(self.figure.data[-1].type, "sankey")
        self.assertEqual(self.figure.data[-1].arrangement, "snap")

        # Check message
        self.figure._send_addTraces_msg.assert_called_once_with(
            [{"type": "sankey", "arrangement": "snap"}]
        )

    def test_add_traces(self):

        # Add two traces
        self.figure.add_traces(
            [
                go.Sankey(arrangement="snap"),
                go.Histogram2dContour(line={"color": "cyan"}),
            ]
        )

        # Check access properties
        self.assertEqual(self.figure.data[-2].type, "sankey")
        self.assertEqual(self.figure.data[-2].arrangement, "snap")

        self.assertEqual(self.figure.data[-1].type, "histogram2dcontour")
        self.assertEqual(self.figure.data[-1].line.color, "cyan")

        # Check message
        new_uid1 = self.figure.data[-2].uid
        new_uid2 = self.figure.data[-1].uid
        self.figure._send_addTraces_msg.assert_called_once_with(
            [
                {"type": "sankey", "arrangement": "snap"},
                {"type": "histogram2dcontour", "line": {"color": "cyan"}},
            ]
        )


def test_add_trace_exclude_empty_subplots():
    # Add traces
    fig = make_subplots(2, 2)
    fig.add_trace(go.Scatter(x=[1, 2, 3], y=[5, 1, 2]), row=1, col=1)
    fig.add_trace(go.Scatter(x=[1, 2, 3], y=[2, 1, -7]), row=2, col=2)
    # Add traces with exclude_empty_subplots set to true and make sure this
    # doesn't add to traces that don't already have data
    fig.add_trace(
        go.Scatter(x=[1, 2, 3], y=[0, 1, -1]),
        row="all",
        col="all",
        exclude_empty_subplots=True,
    )
    assert len(fig.data) == 4
    assert fig.data[2]["xaxis"] == "x" and fig.data[2]["yaxis"] == "y"
    assert fig.data[3]["xaxis"] == "x4" and fig.data[3]["yaxis"] == "y4"


def test_add_trace_no_exclude_empty_subplots():
    # Add traces
    fig = make_subplots(2, 2)
    fig.add_trace(go.Scatter(x=[1, 2, 3], y=[5, 1, 2]), row=1, col=1)
    fig.add_trace(go.Scatter(x=[1, 2, 3], y=[2, 1, -7]), row=2, col=2)
    # Add traces with exclude_empty_subplots set to true and make sure this
    # even adds to traces that don't already have data
    fig.add_trace(go.Scatter(x=[1, 2, 3], y=[0, 1, -1]), row="all", col="all")
    assert len(fig.data) == 6
    assert fig.data[2]["xaxis"] == "x" and fig.data[2]["yaxis"] == "y"
    assert fig.data[3]["xaxis"] == "x2" and fig.data[3]["yaxis"] == "y2"
    assert fig.data[4]["xaxis"] == "x3" and fig.data[4]["yaxis"] == "y3"
    assert fig.data[5]["xaxis"] == "x4" and fig.data[5]["yaxis"] == "y4"


def test_add_trace_exclude_totally_empty_subplots():
    # Add traces
    fig = make_subplots(2, 2)
    fig.add_trace(go.Scatter(x=[1, 2, 3], y=[5, 1, 2]), row=1, col=1)
    fig.add_trace(go.Scatter(x=[1, 2, 3], y=[2, 1, -7]), row=2, col=2)
    fig.add_shape(dict(type="rect", x0=0, x1=1, y0=0, y1=1), row=1, col=2)
    # Add traces with exclude_empty_subplots set to true and make sure this
    # doesn't add to traces that don't already have data or layout objects
    fig.add_trace(
        go.Scatter(x=[1, 2, 3], y=[0, 1, -1]),
        row="all",
        col="all",
        exclude_empty_subplots=["anything", "truthy"],
    )
    assert len(fig.data) == 5
    assert fig.data[2]["xaxis"] == "x" and fig.data[2]["yaxis"] == "y"
    assert fig.data[3]["xaxis"] == "x2" and fig.data[3]["yaxis"] == "y2"
    assert fig.data[4]["xaxis"] == "x4" and fig.data[4]["yaxis"] == "y4"


def test_add_trace_no_exclude_totally_empty_subplots():
    # Add traces
    fig = make_subplots(2, 2)
    fig.add_trace(go.Scatter(x=[1, 2, 3], y=[5, 1, 2]), row=1, col=1)
    fig.add_trace(go.Scatter(x=[1, 2, 3], y=[2, 1, -7]), row=2, col=2)
    fig.add_shape(dict(type="rect", x0=0, x1=1, y0=0, y1=1), row=1, col=2)
    # Add traces with exclude_empty_subplots set to true and make sure this
    # even adds to traces that don't already have data or layout objects
    fig.add_trace(go.Scatter(x=[1, 2, 3], y=[0, 1, -1]), row="all", col="all")
    assert len(fig.data) == 6
    assert fig.data[2]["xaxis"] == "x" and fig.data[2]["yaxis"] == "y"
    assert fig.data[3]["xaxis"] == "x2" and fig.data[3]["yaxis"] == "y2"
    assert fig.data[4]["xaxis"] == "x3" and fig.data[4]["yaxis"] == "y3"
    assert fig.data[5]["xaxis"] == "x4" and fig.data[5]["yaxis"] == "y4"
