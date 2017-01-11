from __future__ import absolute_import

from unittest import TestCase

from plotly import exceptions
from plotly.graph_objs import Figure


class FigureTest(TestCase):

    def test_instantiation(self):

        native_figure = {
            'data': [],
            'layout': {},
            'frames': []
        }

        Figure(native_figure)
        Figure()

    def test_access_top_level(self):

        # Figure is special, we define top-level objects that always exist.

        self.assertEqual(Figure().data, [])
        self.assertEqual(Figure().layout, {})
        self.assertEqual(Figure().frames, [])

    def test_nested_frames(self):
        with self.assertRaisesRegexp(exceptions.PlotlyDictKeyError, 'frames'):
            Figure({'frames': [{'frames': []}]})

        figure = Figure()
        figure.frames = [{}]
        with self.assertRaisesRegexp(exceptions.PlotlyDictKeyError, 'frames'):
            figure.frames[0].frames = []
