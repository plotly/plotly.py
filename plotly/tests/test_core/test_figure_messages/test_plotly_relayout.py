import sys
from unittest import TestCase

import plotly.graph_objs as go

if sys.version_info.major == 3 and sys.version_info.minor >= 3:
    from unittest.mock import MagicMock
else:
    from mock import MagicMock


class TestRelayoutMessage(TestCase):

    def setUp(self):
        # Construct with mocked _send_relayout_msg method
        self.figure = go.Figure(layout={'xaxis': {'range': [-1, 4]}})

        # Mock out the message method
        self.figure._send_relayout_msg = MagicMock()

    def test_property_assignment_toplevel(self):
        self.figure.layout.title = 'hello'
        self.figure._send_relayout_msg.assert_called_once_with(
            {'title': 'hello'})

    def test_property_assignment_nested(self):
        self.figure.layout.xaxis.titlefont.family = 'courier'
        self.figure._send_relayout_msg.assert_called_once_with(
            {'xaxis.titlefont.family': 'courier'})

    def test_property_assignment_nested_subplot2(self):
        # Initialize xaxis2
        self.figure.layout.xaxis2 = {'range': [0, 1]}
        self.figure._send_relayout_msg.assert_called_once_with(
            {'xaxis2': {'range': [0, 1]}})

        # Reset mock and perform property assignment
        self.figure._send_relayout_msg = MagicMock()
        self.figure.layout.xaxis2.titlefont.family = 'courier'
        self.figure._send_relayout_msg.assert_called_once_with(
            {'xaxis2.titlefont.family': 'courier'})

    def test_property_assignment_nested_array(self):

        # Initialize images
        self.figure.layout.updatemenus = [
            {},
            go.layout.Updatemenu(buttons=[
                {}, {}, go.layout.updatemenu.Button(method='relayout')]),
            {}]

        self.figure._send_relayout_msg.assert_called_once_with(
            {'updatemenus': [{}, {'buttons': [
                {}, {}, {'method': 'relayout'}]}, {}]})

        # Reset mock and perform property assignment
        self.figure._send_relayout_msg = MagicMock()
        self.figure.layout.updatemenus[1].buttons[0].method = 'restyle'
        self.figure._send_relayout_msg.assert_called_once_with(
            {'updatemenus.1.buttons.0.method': 'restyle'})

    def test_property_assignment_template(self):
        # Initialize template object
        self.figure.layout.template = {'layout': {
            'xaxis': {'title': 'x-label'}}}
        self.figure._send_relayout_msg.assert_called_with(
            {'template': {'layout': {'xaxis': {'title': 'x-label'}}}})

        # template layout property
        self.figure.layout.template.layout.title = 'Template Title'
        self.figure._send_relayout_msg.assert_called_with(
            {'template.layout.title': 'Template Title'})

        # template add trace
        self.figure.layout.template.data = {'bar': [
            {'marker': {'color': 'blue'}},
            {'marker': {'color': 'yellow'}}]}

        self.figure._send_relayout_msg.assert_called_with(
            {'template.data': {'bar': [
                {'type': 'bar', 'marker': {'color': 'blue'}},
                {'type': 'bar', 'marker': {'color': 'yellow'}}]}})

        # template set trace property
        self.figure.layout.template.data.bar[1].marker.opacity = 0.5
        self.figure._send_relayout_msg.assert_called_with(
            {'template.data.bar.1.marker.opacity': 0.5})

        # Set elementdefaults property
        self.figure.layout.template.layout.imagedefaults.sizex = 300
        self.figure._send_relayout_msg.assert_called_with(
            {'template.layout.imagedefaults.sizex': 300})

    def test_plotly_relayout_toplevel(self):
        self.figure.plotly_relayout({'title': 'hello'})
        self.figure._send_relayout_msg.assert_called_once_with(
            {'title': 'hello'})

    def test_plotly_relayout_nested(self):
        self.figure.plotly_relayout({'xaxis.titlefont.family': 'courier'})
        self.figure._send_relayout_msg.assert_called_once_with(
            {'xaxis.titlefont.family': 'courier'})

    def test_plotly_relayout_nested_subplot2(self):
        # Initialize xaxis2
        self.figure.layout.xaxis2 = {'range': [0, 1]}
        self.figure._send_relayout_msg.assert_called_once_with(
            {'xaxis2': {'range': [0, 1]}})

        # Reset mock and perform property assignment
        self.figure._send_relayout_msg = MagicMock()
        self.figure.plotly_relayout({'xaxis2.titlefont.family': 'courier'})
        self.figure._send_relayout_msg.assert_called_once_with(
            {'xaxis2.titlefont.family': 'courier'})

    def test_plotly_relayout_nested_array(self):

        # Initialize images
        self.figure.layout.updatemenus = [
            {},
            go.layout.Updatemenu(buttons=[
                {}, {}, go.layout.updatemenu.Button(method='relayout')]),
            {}]

        self.figure._send_relayout_msg.assert_called_once_with(
            {'updatemenus': [{}, {'buttons': [
                {}, {}, {'method': 'relayout'}]}, {}]})

        # Reset mock and perform property assignment
        self.figure._send_relayout_msg = MagicMock()

        self.figure.plotly_relayout(
            {'updatemenus[1].buttons.0.method': 'restyle'})
        self.figure._send_relayout_msg.assert_called_once_with(
            {'updatemenus[1].buttons.0.method': 'restyle'})
