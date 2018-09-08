from __future__ import absolute_import

from unittest import TestCase
import plotly.graph_objs as go
from collections import OrderedDict


class FigureTest(TestCase):

    def test_to_ordered_dict(self):

        fig = go.Figure(layout={'yaxis': {'range': [1, 2]},
                                'xaxis': {'range': [1, 2]},
                                'shapes': [{'xsizemode': 'pixel',
                                            'type': 'circle'},
                                           {'type': 'line',
                                            'xsizemode': 'pixel'}]},
                        data=[{'type': 'scatter',
                               'marker': {'size': 12, 'color': 'green'}},
                              {'type': 'bar',
                               'y': [1, 2],
                               'x': [1, 2]}])

        result = fig.to_ordered_dict()

        expected = OrderedDict([('data', [
            OrderedDict([('marker',
                          OrderedDict([('color', 'green'), ('size', 12)])),
                         ('type', 'scatter')]),
            OrderedDict([('type', 'bar'),
                         ('x', [1, 2]),
                         ('y', [1, 2])])]),
                                ('layout',OrderedDict([
                                    ('shapes', [
                                        OrderedDict([
                                            ('type', 'circle'),
                                            ('xsizemode', 'pixel')]),
                                        OrderedDict([
                                            ('type', 'line'),
                                            ('xsizemode', 'pixel')])]),
                                    ('xaxis', OrderedDict(
                                        [('range', [1, 2])])),
                                    ('yaxis', OrderedDict(
                                        [('range', [1, 2])]))
                                ]))])

        self.assertEqual(result, expected)

    def test_to_ordered_with_frames(self):
        frame = go.Frame(layout={'yaxis': {'range': [1, 2]},
                                 'xaxis': {'range': [1, 2]},
                                 'shapes': [{'xsizemode': 'pixel',
                                             'type': 'circle'},
                                            {'type': 'line',
                                             'xsizemode': 'pixel'}]},
                         data=[{'type': 'scatter',
                                'marker': {'size': 12, 'color': 'green'}},
                               {'type': 'bar',
                                'y': [1, 2],
                                'x': [1, 2]}])

        fig = go.Figure(frames=[{}, frame])
        result = fig.to_ordered_dict()

        expected_frame = OrderedDict([('data', [
            OrderedDict([('marker',
                          OrderedDict([('color', 'green'), ('size', 12)])),
                         ('type', 'scatter')]),
            OrderedDict([('type', 'bar'),
                         ('x', [1, 2]),
                         ('y', [1, 2])])]),
                                      ('layout', OrderedDict([
                                          ('shapes', [
                                              OrderedDict([
                                                  ('type', 'circle'),
                                                  ('xsizemode', 'pixel')]),
                                              OrderedDict([
                                                  ('type', 'line'),
                                                  ('xsizemode', 'pixel')])]),
                                          ('xaxis', OrderedDict(
                                              [('range', [1, 2])])),
                                          ('yaxis', OrderedDict(
                                              [('range', [1, 2])]))
                                      ]))])

        expected = OrderedDict([('data', []),
                                ('layout', OrderedDict()),
                                ('frames', [OrderedDict(),
                                            expected_frame])])

        self.assertEqual(result, expected)
