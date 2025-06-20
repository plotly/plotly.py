from unittest import TestCase

from plotly.graph_objs import Bar, Frames, Frame, Layout

import pytest

import re


def return_prop_descriptions(prop_descrip_text):
    raw_matches = re.findall("\n        [a-z]+|        [a-z]+\n", prop_descrip_text)
    matches = []
    for r in raw_matches:
        r = r.replace(" ", "")
        r = r.replace("\n", "")
        matches.append(r)
    return matches


class FramesTest(TestCase):
    def test_instantiation(self):
        native_frames = [
            {},
            {"data": []},
            "foo",
            {"data": [], "group": "baz", "layout": {}, "name": "hoopla"},
        ]

        Frames(native_frames)
        Frames()

    def test_non_string_frame(self):
        frames = Frames()
        frames.append({})

        # TODO: Decide if errors should be thrown
        # with self.assertRaises(exceptions.PlotlyListEntryError):
        #     frames.append([])

        # with self.assertRaises(exceptions.PlotlyListEntryError):
        #     frames.append(0)

    @pytest.mark.nodev
    def test_deeply_nested_layout_attributes(self):
        frames = Frame
        frames.layout = [Layout()]
        frames.layout[0].xaxis.showexponent = "all"
        prop_descrip_text = frames.layout[0].font._prop_descriptions

        matches = return_prop_descriptions(prop_descrip_text)

        # It's OK if this needs to change, but we should check *something*.
        self.assertEqual(
            set(matches),
            {
                "color",
                "family",
                "size",
                "weight",
                "variant",
                "style",
                "textcase",
                "lineposition",
                "shadow",
            },
        )

    def test_deeply_nested_data_attributes(self):
        frames = Frame
        frames.data = [Bar()]
        frames.data[0].marker.color = "red"

        # parse out valid attrs from ._prop_descriptions
        prop_descrip_text = frames.data[0].marker.line._prop_descriptions

        matches = return_prop_descriptions(prop_descrip_text)

        # Skip 'cmid' that is going to be added in plotly.js 1.45.0
        matches = [m for m in matches if m != "cmid"]

        # It's OK if this needs to change, but we should check *something*.
        self.assertEqual(
            set(matches),
            {
                "colorsrc",
                "autocolorscale",
                "cmin",
                "colorscale",
                "color",
                "reversescale",
                "width",
                "cauto",
                "widthsrc",
                "cmax",
                "coloraxis",
            },
        )

    def test_frame_only_attrs(self):
        frames = Frame
        frames.frame = [Frame()]

        # It's OK if this needs to change, but we should check *something*.
        prop_descrip_text = frames.frame[0]._prop_descriptions

        matches = return_prop_descriptions(prop_descrip_text)

        self.assertEqual(
            set(matches), {"group", "name", "data", "layout", "baseframe", "traces"}
        )
