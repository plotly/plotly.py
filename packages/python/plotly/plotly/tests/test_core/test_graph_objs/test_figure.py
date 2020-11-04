from __future__ import absolute_import

import plotly.graph_objects as go
from plotly.subplots import make_subplots
from plotly.tests.utils import TestCaseNoTemplate
import pytest


class FigureTest(TestCaseNoTemplate):
    def setUp(self):
        import plotly.io as pio

        pio.templates.default = None

    def test_instantiation(self):

        native_figure = {"data": [], "layout": {}, "frames": []}

        go.Figure(native_figure)
        go.Figure()

    def test_access_top_level(self):

        # Figure is special, we define top-level objects that always exist.

        self.assertEqual(go.Figure().data, ())
        self.assertEqual(go.Figure().layout.to_plotly_json(), {})
        self.assertEqual(go.Figure().frames, ())

    def test_nested_frames(self):
        with self.assertRaisesRegexp(ValueError, "frames"):
            go.Figure({"frames": [{"frames": []}]})

        figure = go.Figure()
        figure.frames = [{}]

        with self.assertRaisesRegexp(ValueError, "frames"):
            figure.to_plotly_json()["frames"][0]["frames"] = []
            figure.frames[0].frames = []

    def test_raises_invalid_property_name(self):
        with self.assertRaises(ValueError):
            go.Figure(
                data=[{"type": "bar", "bogus": 123}],
                layout={"bogus": 23, "title": "Figure title"},
                frames=[
                    {
                        "data": [{"type": "bar", "bogus": 123}],
                        "layout": {"bogus": 23, "title": "Figure title"},
                    }
                ],
            )

    def test_skip_invalid_property_name(self):
        fig = go.Figure(
            data=[{"type": "bar", "bogus": 123}],
            layout={"bogus": 23, "title": {"text": "Figure title"}},
            frames=[
                {
                    "data": [{"type": "bar", "bogus": 123}],
                    "layout": {"bogus": 23, "title": "Figure title"},
                }
            ],
            bogus=123,
            skip_invalid=True,
        )

        fig_dict = fig.to_dict()

        # Remove trace uid property
        for trace in fig_dict["data"]:
            trace.pop("uid", None)

        self.assertEqual(fig_dict["data"], [{"type": "bar"}])
        self.assertEqual(fig_dict["layout"], {"title": {"text": "Figure title"}})
        self.assertEqual(
            fig_dict["frames"],
            [
                {
                    "data": [{"type": "bar"}],
                    "layout": {"title": {"text": "Figure title"}},
                }
            ],
        )

    def test_raises_invalid_property_value(self):
        with self.assertRaises(ValueError):
            go.Figure(
                data=[{"type": "bar", "showlegend": "bad_value"}],
                layout={"paper_bgcolor": "bogus_color", "title": "Figure title"},
                frames=[
                    {
                        "data": [{"type": "bar", "showlegend": "bad_value"}],
                        "layout": {"bgcolor": "bad_color", "title": "Figure title"},
                    }
                ],
            )

    def test_skip_invalid_property_value(self):
        fig = go.Figure(
            data=[{"type": "bar", "showlegend": "bad_value"}],
            layout={"paper_bgcolor": "bogus_color", "title": "Figure title"},
            frames=[
                {
                    "data": [{"type": "bar", "showlegend": "bad_value"}],
                    "layout": {"bgcolor": "bad_color", "title": "Figure title"},
                }
            ],
            skip_invalid=True,
        )

        fig_dict = fig.to_dict()

        # Remove trace uid property
        for trace in fig_dict["data"]:
            trace.pop("uid", None)

        self.assertEqual(fig_dict["data"], [{"type": "bar"}])
        self.assertEqual(fig_dict["layout"], {"title": {"text": "Figure title"}})
        self.assertEqual(
            fig_dict["frames"],
            [
                {
                    "data": [{"type": "bar"}],
                    "layout": {"title": {"text": "Figure title"}},
                }
            ],
        )

    def test_raises_invalid_toplevel_kwarg(self):
        with self.assertRaises(TypeError):
            go.Figure(
                data=[{"type": "bar"}],
                layout={"title": "Figure title"},
                frames=[
                    {"data": [{"type": "bar"}], "layout": {"title": "Figure title"}}
                ],
                bogus=123,
            )

    def test_toplevel_underscore_kwarg(self):
        fig = go.Figure(
            data=[{"type": "bar"}], layout_title_text="Hello, Figure title!"
        )

        self.assertEqual(fig.layout.title.text, "Hello, Figure title!")

    def test_add_trace_underscore_kwarg(self):
        fig = go.Figure()

        fig.add_scatter(y=[2, 1, 3], marker_line_color="green")

        self.assertEqual(fig.data[0].marker.line.color, "green")

    def test_scalar_trace_as_data(self):
        fig = go.Figure(data=go.Waterfall(y=[2, 1, 3]))
        self.assertEqual(fig.data, (go.Waterfall(y=[2, 1, 3]),))

        fig = go.Figure(data=dict(type="waterfall", y=[2, 1, 3]))
        self.assertEqual(fig.data, (go.Waterfall(y=[2, 1, 3]),))

    def test_pop_data(self):
        fig = go.Figure(data=go.Waterfall(y=[2, 1, 3]))
        self.assertEqual(fig.pop("data"), (go.Waterfall(y=[2, 1, 3]),))
        self.assertEqual(fig.data, ())

    def test_pop_layout(self):
        fig = go.Figure(layout=go.Layout(width=1000))
        self.assertEqual(fig.pop("layout"), go.Layout(width=1000))
        self.assertEqual(fig.layout, go.Layout())

    def test_pop_invalid_key(self):
        fig = go.Figure(layout=go.Layout(width=1000))
        with self.assertRaises(KeyError):
            fig.pop("bogus")

    def test_update_overwrite_layout(self):
        fig = go.Figure(layout=go.Layout(width=1000))

        # By default, update works recursively so layout.width should remain
        fig.update(layout={"title": {"text": "Fig Title"}})
        fig.layout.pop("template")
        self.assertEqual(
            fig.layout.to_plotly_json(), {"title": {"text": "Fig Title"}, "width": 1000}
        )

        # With overwrite=True, all existing layout properties should be
        # removed
        fig.update(overwrite=True, layout={"title": {"text": "Fig2 Title"}})
        fig.layout.pop("template")
        self.assertEqual(fig.layout.to_plotly_json(), {"title": {"text": "Fig2 Title"}})

    def test_update_overwrite_data(self):
        fig = go.Figure(
            data=[go.Bar(marker_color="blue"), go.Bar(marker_color="yellow")]
        )

        fig.update(overwrite=True, data=[go.Marker(y=[1, 3, 2], line_color="yellow")])

        self.assertEqual(
            fig.to_plotly_json()["data"],
            [{"type": "scatter", "y": [1, 3, 2], "line": {"color": "yellow"}}],
        )


def test_set_subplots():
    # Test that it works the same as make_subplots for a simple call
    fig0 = go.Figure()
    fig0_sp = make_subplots(2, 2)
    fig0.set_subplots(2, 2)
    assert fig0.layout == fig0_sp.layout
    # Test that it accepts the same arguments as make_subplots
    fig1 = go.Figure()
    fig1.set_subplots(rows=2, cols=2, horizontal_spacing=0.25, vertical_spacing=0.1)
    fig1_sp = make_subplots(
        rows=2, cols=2, horizontal_spacing=0.25, vertical_spacing=0.1
    )
    assert fig1.layout == fig1_sp.layout
    # Test that calling on a figure that already has subplots throws an error.
    with pytest.raises(ValueError, match=r"^This figure already has subplots\.$"):
        fig1.set_subplots(2, 3)
