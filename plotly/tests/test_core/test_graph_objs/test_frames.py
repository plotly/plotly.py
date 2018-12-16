from __future__ import absolute_import

from unittest import TestCase

from plotly import exceptions
from plotly.graph_objs import Bar, Frames


class FramesTest(TestCase):

    def test_instantiation(self):

        native_frames = [
            {},
            {'data': []},
            'foo',
            {'data': [], 'group': 'baz', 'layout': {}, 'name': 'hoopla'}
        ]

        Frames(native_frames)
        Frames()

    def test_string_frame(self):
        frames = Frames()
        frames.append({'group': 'baz', 'data': []})
        frames.append('foobar')
        self.assertEqual(frames[1], 'foobar')
        self.assertEqual(frames.to_string(),
                         "Frames([\n"
                         "    dict(\n"
                         "        data=Data(),\n"
                         "        group='baz'\n"
                         "    ),\n"
                         "    'foobar'\n"
                         "])")

    def test_non_string_frame(self):
        frames = Frames()
        frames.append({})

        with self.assertRaises(exceptions.PlotlyListEntryError):
            frames.append([])

        with self.assertRaises(exceptions.PlotlyListEntryError):
            frames.append(0)

    def test_deeply_nested_layout_attributes(self):
        frames = Frames()
        frames.append({})
        frames[0].layout.xaxis.showexponent = 'all'

        # It's OK if this needs to change, but we should check *something*.
        self.assertEqual(
            frames[0].layout.font._get_valid_attributes(),
            {'color', 'family', 'size'}
        )

    def test_deeply_nested_data_attributes(self):
        frames = Frames()
        frames.append({})
        frames[0].data = [Bar()]
        frames[0].data[0].marker.color = 'red'

        # It's OK if this needs to change, but we should check *something*.
        self.assertEqual(
            frames[0].data[0].marker.line._get_valid_attributes(),
            {'colorsrc', 'autocolorscale', 'cmin', 'colorscale', 'color',
             'reversescale', 'width', 'cauto', 'widthsrc', 'cmax'}
        )

    def test_frame_only_attrs(self):
        frames = Frames()
        frames.append({})

        # It's OK if this needs to change, but we should check *something*.
        self.assertEqual(
            frames[0]._get_valid_attributes(),
            {'group', 'name', 'data', 'layout', 'baseframe', 'traces'}
        )
