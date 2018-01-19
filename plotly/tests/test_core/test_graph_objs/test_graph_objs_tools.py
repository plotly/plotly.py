from __future__ import absolute_import

from unittest import TestCase

from plotly import graph_reference as gr
from plotly.graph_objs import graph_objs_tools as got
from plotly import graph_objs as go


class TestGetHelp(TestCase):

    def test_get_help_does_not_raise(self):

        msg = None
        try:
            for object_name in gr.OBJECTS:
                msg = object_name
                got.get_help(object_name)

            for object_name in gr.ARRAYS:
                msg = object_name
                got.get_help(object_name)

            for object_name in gr.OBJECTS:
                attributes = gr.get_valid_attributes(object_name)
                for attribute in attributes:
                    msg = (object_name, attribute)
                    got.get_help(object_name, attribute=attribute)
                fake_attribute = 'fake attribute'
                msg = (object_name, fake_attribute)
                got.get_help(object_name, attribute=fake_attribute)
        except:
            self.fail(msg=msg)


class TestKeyParts(TestCase):
    def test_without_underscore_attr(self):
        assert got._key_parts("foo") == ["foo"]
        assert got._key_parts("foo_bar") == ["foo", "bar"]
        assert got._key_parts("foo_bar_baz") == ["foo", "bar", "baz"]

    def test_traililng_underscore_attr(self):
        assert got._key_parts("foo_error_x") == ["foo", "error_x"]
        assert got._key_parts("foo_bar_error_x") == ["foo", "bar", "error_x"]
        assert got._key_parts("foo_bar_baz_error_x") == ["foo", "bar", "baz", "error_x"]

    def test_leading_underscore_attr(self):
        assert got._key_parts("error_x_foo") == ["error_x", "foo"]
        assert got._key_parts("error_x_foo_bar") == ["error_x", "foo", "bar"]
        assert got._key_parts("error_x_foo_bar_baz") == ["error_x", "foo", "bar", "baz"]


class TestUnderscoreMagicDictObj(TestCase):

    def test_can_split_string_key_into_parts(self):
        obj1 = {}
        obj2 = {}
        got._underscore_magic("marker_line_width", 42, obj1)
        got._underscore_magic(["marker", "line", "width"], 42, obj2)
        want = {"marker": {"line": {"width": 42}}}
        assert obj1 == obj2 == want

    def test_will_make_tree_with_empty_dict_val(self):
        obj = {}
        got._underscore_magic("marker_colorbar_tickfont", {}, obj)
        assert obj == {"marker": {"colorbar": {"tickfont": {}}}}

    def test_can_set_at_depths_1to4(self):
        # 1 level
        obj = {}
        got._underscore_magic("opacity", 0.9, obj)
        assert obj == {"opacity": 0.9}

        # 2 levels
        got._underscore_magic("line_width", 10, obj)
        assert obj == {"opacity": 0.9, "line": {"width": 10}}

        # 3 levels
        got._underscore_magic("hoverinfo_font_family", "Times", obj)
        want = {
            "opacity": 0.9,
            "line": {"width": 10},
            "hoverinfo": {"font": {"family": "Times"}}
        }
        assert obj == want

        # 4 levels
        got._underscore_magic("marker_colorbar_tickfont_family", "Times", obj)
        want = {
            "opacity": 0.9,
            "line": {"width": 10},
            "hoverinfo": {"font": {"family": "Times"}},
            "marker": {"colorbar": {"tickfont": {"family": "Times"}}},
        }
        assert obj == want

    def test_does_not_displace_existing_fields(self):
        obj = {}
        got._underscore_magic("marker_size", 10, obj)
        got._underscore_magic("marker_line_width", 0.4, obj)
        assert obj == {"marker": {"size": 10, "line": {"width": 0.4}}}

    def test_doesnt_mess_up_underscore_attrs(self):
        obj = {}
        got._underscore_magic("error_x_color", "red", obj)
        got._underscore_magic("error_x_width", 4, obj)
        assert obj == {"error_x": {"color": "red", "width": 4}}


class TestUnderscoreMagicPlotlyDictObj(TestCase):

    def test_can_split_string_key_into_parts(self):
        obj1 = go.Scatter()
        obj2 = go.Scatter()
        got._underscore_magic("marker_line_width", 42, obj1)
        got._underscore_magic(["marker", "line", "width"], 42, obj2)
        want = go.Scatter({"marker": {"line": {"width": 42}}})
        assert obj1 == obj2 == want

    def test_will_make_tree_with_empty_dict_val(self):
        obj = go.Scatter()
        got._underscore_magic("marker_colorbar_tickfont", {}, obj)
        want = go.Scatter({"marker": {"colorbar": {"tickfont": {}}}})
        assert obj == want

    def test_can_set_at_depths_1to4(self):
        # 1 level
        obj = go.Scatter()
        got._underscore_magic("opacity", 0.9, obj)
        assert obj == go.Scatter({"type": "scatter", "opacity": 0.9})

        # 2 levels
        got._underscore_magic("line_width", 10, obj)
        assert obj == go.Scatter({"opacity": 0.9, "line": {"width": 10}})

        # 3 levels
        got._underscore_magic("hoverinfo_font_family", "Times", obj)
        want = go.Scatter({
            "opacity": 0.9,
            "line": {"width": 10},
            "hoverinfo": {"font": {"family": "Times"}}
        })
        assert obj == want

        # 4 levels
        got._underscore_magic("marker_colorbar_tickfont_family", "Times", obj)
        want = go.Scatter({
            "opacity": 0.9,
            "line": {"width": 10},
            "hoverinfo": {"font": {"family": "Times"}},
            "marker": {"colorbar": {"tickfont": {"family": "Times"}}},
        })
        assert obj == want

    def test_does_not_displace_existing_fields(self):
        obj = go.Scatter()
        got._underscore_magic("marker_size", 10, obj)
        got._underscore_magic("marker_line_width", 0.4, obj)
        assert obj == go.Scatter({"marker": {"size": 10, "line": {"width": 0.4}}})

    def test_doesnt_mess_up_underscore_attrs(self):
        obj = go.Scatter()
        got._underscore_magic("error_x_color", "red", obj)
        got._underscore_magic("error_x_width", 4, obj)
        assert obj == go.Scatter({"error_x": {"color": "red", "width": 4}})


class TestAttr(TestCase):
    def test_with_no_positional_argument(self):
        have = got.attr(
            opacity=0.9, line_width=10,
            hoverinfo_font_family="Times",
            marker_colorbar_tickfont_size=10
        )
        want = {
            "opacity": 0.9,
            "line": {"width": 10},
            "hoverinfo": {"font": {"family": "Times"}},
            "marker": {"colorbar": {"tickfont": {"size": 10}}},
        }
        assert have == want

    def test_with_dict_positional_argument(self):
        have = {"x": [1, 2, 3, 4, 5]}
        got.attr(have,
            opacity=0.9, line_width=10,
            hoverinfo_font_family="Times",
            marker_colorbar_tickfont_size=10
        )
        want = {
            "x": [1, 2, 3, 4, 5],
            "opacity": 0.9,
            "line": {"width": 10},
            "hoverinfo": {"font": {"family": "Times"}},
            "marker": {"colorbar": {"tickfont": {"size": 10}}},
        }
        assert have == want

    def test_with_PlotlyDict_positional_argument(self):
        have = go.Scatter({"x": [1, 2, 3, 4, 5]})
        got.attr(have,
            opacity=0.9, line_width=10,
            hoverinfo_font_family="Times",
            marker_colorbar_tickfont_size=10
        )
        want = go.Scatter({
            "x": [1, 2, 3, 4, 5],
            "opacity": 0.9,
            "line": {"width": 10},
            "hoverinfo": {"font": {"family": "Times"}},
            "marker": {"colorbar": {"tickfont": {"size": 10}}},
        })
        assert have == want
