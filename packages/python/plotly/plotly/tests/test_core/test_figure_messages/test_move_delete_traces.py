import sys
from unittest import TestCase
from nose.tools import raises

import plotly.graph_objs as go

if sys.version_info.major == 3 and sys.version_info.minor >= 3:
    from unittest.mock import MagicMock
else:
    from mock import MagicMock


class TestMoveDeleteTracesMessages(TestCase):
    def setUp(self):
        # Construct initial scatter object
        self.figure = go.Figure(data=[
            go.Scatter(y=[3, 2, 1], marker={'color': 'green'}),
            go.Bar(y=[3, 2, 1, 0, -1], marker={'opacity': 0.5}),
            go.Sankey(arrangement='snap')
        ])

        # Mock out the message methods
        self.figure._send_moveTraces_msg = MagicMock()
        self.figure._send_deleteTraces_msg = MagicMock()

    def test_move_traces_swap(self):

        # Swap first and last trace
        traces = self.figure.data
        self.figure.data = [traces[2], traces[1], traces[0]]

        # Check messages
        self.figure._send_moveTraces_msg.assert_called_once_with(
            [0, 1, 2], [2, 1, 0])
        self.assertFalse(self.figure._send_deleteTraces_msg.called)

    def test_move_traces_cycle(self):

        # Cycle traces forward
        traces = self.figure.data
        self.figure.data = [traces[2], traces[0], traces[1]]

        # Check messages
        self.figure._send_moveTraces_msg.assert_called_once_with(
            [0, 1, 2], [1, 2, 0])
        self.assertFalse(self.figure._send_deleteTraces_msg.called)

    def test_delete_single_traces(self):
        # Delete middle trace
        traces = self.figure.data
        self.figure.data = [traces[0], traces[2]]

        # Check messages
        self.figure._send_deleteTraces_msg.assert_called_once_with([1])
        self.assertFalse(self.figure._send_moveTraces_msg.called)

    def test_delete_multiple_traces(self):
        # Delete middle trace
        traces = self.figure.data
        self.figure.data = [traces[1]]

        # Check messages
        self.figure._send_deleteTraces_msg.assert_called_once_with([0, 2])
        self.assertFalse(self.figure._send_moveTraces_msg.called)

    def test_delete_all_traces(self):
        # Delete middle trace
        self.figure.data = []

        # Check messages
        self.figure._send_deleteTraces_msg.assert_called_once_with([0, 1, 2])
        self.assertFalse(self.figure._send_moveTraces_msg.called)

    def test_move_and_delete_traces(self):
        # Delete middle trace
        traces = self.figure.data
        self.figure.data = [traces[2], traces[0]]

        # Check messages
        self.figure._send_deleteTraces_msg.assert_called_once_with([1])
        self.figure._send_moveTraces_msg.assert_called_once_with(
            [0, 1], [1, 0])

    @raises(ValueError)
    def test_validate_assigned_traces_are_subset(self):
        traces = self.figure.data
        self.figure.data = [traces[2],
                            go.Scatter(y=[3, 2, 1]),
                            traces[1]]

    @raises(ValueError)
    def test_validate_assigned_traces_are_not_duplicates(self):
        traces = self.figure.data
        self.figure.data = [traces[2],
                            traces[1],
                            traces[1]]