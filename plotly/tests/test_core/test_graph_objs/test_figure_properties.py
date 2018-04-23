from unittest import TestCase
import plotly.graph_objs as go
from nose.tools import raises


class TestFigureProperties(TestCase):

    def setUp(self):
        # Construct initial scatter object
        self.figure = go.Figure(data=[go.Scatter(y=[3, 2, 1],
                                                 marker={'color': 'green'})],
                                layout={'xaxis': {'range': [-1, 4]}},
                                frames=[go.Frame(
                                    layout={'yaxis':
                                            {'title': 'f1'}})])

    def test_attr_access(self):
        scatt_uid = self.figure.data[0].uid
        self.assertEqual(self.figure.data,
                         (go.Scatter(y=[3, 2, 1],
                                     marker={'color': 'green'},
                                     uid=scatt_uid),))

        self.assertEqual(self.figure.layout,
                         go.Layout(xaxis={'range': [-1, 4]}))

        self.assertEqual(self.figure.frames,
                         (go.Frame(
                             layout={'yaxis': {'title': 'f1'}}),))

    def test_contains(self):
        self.assertIn('data', self.figure)
        self.assertIn('layout', self.figure)
        self.assertIn('frames', self.figure)

    def test_iter(self):
        self.assertEqual(set(self.figure), {'data', 'layout', 'frames'})

    def test_attr_item(self):

        # test that equal objects can be retrieved using attr or item
        # syntax
        self.assertEqual(self.figure.data, self.figure['data'])
        self.assertEqual(self.figure.layout, self.figure['layout'])
        self.assertEqual(self.figure.frames, self.figure['frames'])

    def test_property_assignment_tuple(self):

        # Empty
        self.assertIs(self.figure[()], self.figure)

        # Layout
        self.figure[('layout', 'xaxis', 'range')] = (-10, 10)
        self.assertEqual(self.figure[('layout', 'xaxis', 'range')], (-10, 10))

        # Data
        self.figure[('data', 0, 'marker', 'color')] = 'red'
        self.assertEqual(self.figure[('data', 0, 'marker', 'color')], 'red')

        # Frames
        self.figure[('frames', 0, 'layout', 'yaxis', 'title')] = 'f2'
        self.assertEqual(
            self.figure[('frames', 0, 'layout', 'yaxis', 'title')], 'f2')

    def test_property_assignment_dots(self):
        # Layout
        self.figure['layout.xaxis.range'] = (-10, 10)
        self.assertEqual(self.figure['layout.xaxis.range'], (-10, 10))

        # Data
        self.figure['data.0.marker.color'] = 'red'
        self.assertEqual(self.figure['data[0].marker.color'], 'red')

        # Frames
        self.figure['frames[0].layout.yaxis.title'] = 'f2'
        self.assertEqual(
            self.figure['frames.0.layout.yaxis.title'], 'f2')

    def test_update_layout(self):
        # Check initial x-range
        self.assertEqual(self.figure.layout.xaxis.range, (-1, 4))

        # Update with kwarg
        self.figure.update(layout={'xaxis': {'range': [10, 20]}})
        self.assertEqual(self.figure.layout.xaxis.range, (10, 20))

        # Update with dict
        self.figure.update({'layout': {'xaxis': {'range': [100, 200]}}})
        self.assertEqual(self.figure.layout.xaxis.range, (100, 200))

    def test_update_data(self):
        # Check initial marker color
        self.assertEqual(self.figure.data[0].marker.color, 'green')

        # Update with dict kwarg
        self.figure.update(data={0: {'marker': {'color': 'blue'}}})
        self.assertEqual(self.figure.data[0].marker.color, 'blue')

        # Update with list kwarg
        self.figure.update(data=[{'marker': {'color': 'red'}}])
        self.assertEqual(self.figure.data[0].marker.color, 'red')

        # Update with dict
        self.figure.update({'data': {0: {'marker': {'color': 'yellow'}}}})
        self.assertEqual(self.figure.data[0].marker.color, 'yellow')

    def test_update_frames(self):
        # Check initial frame axis title
        self.assertEqual(self.figure.frames[0].layout.yaxis.title, 'f1')

        # Update with dict kwarg
        self.figure.update(frames={0: {'layout': {'yaxis': {'title': 'f2'}}}})
        self.assertEqual(self.figure.frames[0].layout.yaxis.title, 'f2')

        # Update with list kwarg
        self.figure.update(frames=[{'layout': {'yaxis': {'title': 'f3'}}}])
        self.assertEqual(self.figure.frames[0].layout.yaxis.title, 'f3')

        # Update with dict
        self.figure.update({'frames':
                            [{'layout': {'yaxis': {'title': 'f4'}}}]})
        self.assertEqual(self.figure.frames[0].layout.yaxis.title, 'f4')

    @raises(AttributeError)
    def test_access_invalid_attr(self):
        self.figure.bogus

    @raises(KeyError)
    def test_access_invalid_item(self):
        self.figure['bogus']

    @raises(AttributeError)
    def test_assign_invalid_attr(self):
        self.figure.bogus = 'val'

    @raises(KeyError)
    def test_access_invalid_item(self):
        self.figure['bogus'] = 'val'
