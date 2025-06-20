from unittest import TestCase
import pytest

import plotly.graph_objs as go
import plotly.io as pio


class TestFigureProperties(TestCase):
    def setUp(self):
        # Disable default template
        pio.templates.default = None

        # Construct initial scatter object
        self.figure = go.Figure(
            data=[go.Scatter(y=[3, 2, 1], marker={"color": "green"})],
            layout={"xaxis": {"range": [-1, 4]}},
            frames=[go.Frame(layout={"yaxis": {"title": "f1"}})],
        )

    def tearDown(self):
        # Reenable default template
        pio.templates.default = "plotly"

    def test_attr_access(self):
        scatt_uid = self.figure.data[0].uid
        self.assertEqual(
            self.figure.data,
            (go.Scatter(y=[3, 2, 1], marker={"color": "green"}, uid=scatt_uid),),
        )

        self.assertEqual(self.figure.layout, go.Layout(xaxis={"range": [-1, 4]}))

        self.assertEqual(
            self.figure.frames, (go.Frame(layout={"yaxis": {"title": "f1"}}),)
        )

    def test_contains(self):
        self.assertIn("data", self.figure)
        self.assertIn("layout", self.figure)
        self.assertIn("frames", self.figure)

    def test_iter(self):
        self.assertEqual(set(self.figure), {"data", "layout", "frames"})

    def test_attr_item(self):
        # test that equal objects can be retrieved using attr or item
        # syntax
        self.assertEqual(self.figure.data, self.figure["data"])
        self.assertEqual(self.figure.layout, self.figure["layout"])
        self.assertEqual(self.figure.frames, self.figure["frames"])

    def test_property_assignment_tuple(self):
        # Empty
        self.assertIs(self.figure[()], self.figure)

        # Layout
        self.figure[("layout", "xaxis", "range")] = (-10, 10)
        self.assertEqual(self.figure[("layout", "xaxis", "range")], (-10, 10))

        # Data
        self.figure[("data", 0, "marker", "color")] = "red"
        self.assertEqual(self.figure[("data", 0, "marker", "color")], "red")

        # Frames
        self.figure[("frames", 0, "layout", "yaxis", "title", "text")] = "f2"
        self.assertEqual(
            self.figure[("frames", 0, "layout", "yaxis", "title", "text")], "f2"
        )

    def test_property_assignment_dots(self):
        # Layout
        self.figure["layout.xaxis.range"] = (-10, 10)
        self.assertEqual(self.figure["layout.xaxis.range"], (-10, 10))

        # Data
        self.figure["data.0.marker.color"] = "red"
        self.assertEqual(self.figure["data[0].marker.color"], "red")

        # Frames
        self.figure["frames[0].layout.yaxis.title.text"] = "f2"
        self.assertEqual(self.figure["frames.0.layout.yaxis.title.text"], "f2")

    def test_access_invalid_attr(self):
        with pytest.raises(AttributeError):
            self.figure.bogus

    def test_access_invalid_item(self):
        with pytest.raises(KeyError):
            self.figure["bogus"]

    def test_assign_invalid_attr(self):
        with pytest.raises(AttributeError):
            self.figure.bogus = "val"

    def test_assign_invalid_item(self):
        with pytest.raises(KeyError):
            self.figure["bogus"] = "val"

    # Update
    def test_update_layout(self):
        # Check initial x-range
        self.assertEqual(self.figure.layout.xaxis.range, (-1, 4))

        # Update with kwarg
        self.figure.update(layout={"xaxis": {"range": [10, 20]}})
        self.assertEqual(self.figure.layout.xaxis.range, (10, 20))

        # Update with dict
        self.figure.update({"layout": {"xaxis": {"range": [100, 200]}}})
        self.assertEqual(self.figure.layout.xaxis.range, (100, 200))

    def test_update_data(self):
        # Check initial marker color
        self.assertEqual(self.figure.data[0].marker.color, "green")

        # Update with dict kwarg
        self.figure.update(data={0: {"marker": {"color": "blue"}}})
        self.assertEqual(self.figure.data[0].marker.color, "blue")

        # Update with list kwarg
        self.figure.update(data=[{"marker": {"color": "red"}}])
        self.assertEqual(self.figure.data[0].marker.color, "red")

        # Update with dict
        self.figure.update({"data": {0: {"marker": {"color": "yellow"}}}})
        self.assertEqual(self.figure.data[0].marker.color, "yellow")

    def test_update_data_dots(self):
        # Check initial marker color
        self.assertEqual(self.figure.data[0].marker.color, "green")

        # Update with dict kwarg
        self.figure.update(data={0: {"marker.color": "blue"}})
        self.assertEqual(self.figure.data[0].marker.color, "blue")

        # Update with list kwarg
        self.figure.update(data=[{"marker.color": "red"}])
        self.assertEqual(self.figure.data[0].marker.color, "red")

        # Update with dict
        self.figure.update({"data[0].marker.color": "yellow"})
        self.assertEqual(self.figure.data[0].marker.color, "yellow")

    def test_update_data_underscores(self):
        # Check initial marker color
        self.assertEqual(self.figure.data[0].marker.color, "green")

        # Update with dict kwarg
        self.figure.update(data={0: {"marker_color": "blue"}})
        self.assertEqual(self.figure.data[0].marker.color, "blue")

        # Update with list kwarg
        self.figure.update(data=[{"marker_color": "red"}])
        self.assertEqual(self.figure.data[0].marker.color, "red")

        # Update with dict
        self.figure.update({"data_0_marker_color": "yellow"})
        self.assertEqual(self.figure.data[0].marker.color, "yellow")

        # Update with kwarg
        self.figure.update(data_0_marker_color="yellow")
        self.assertEqual(self.figure.data[0].marker.color, "yellow")

    def test_update_data_empty(self):
        # Create figure with empty data (no traces)
        figure = go.Figure(layout={"width": 1000})

        # Update data with new traces
        figure.update(data=[go.Scatter(y=[2, 1, 3]), go.Bar(y=[1, 2, 3])])

        # Build expected dict
        expected = {
            "data": [
                {"y": [2, 1, 3], "type": "scatter"},
                {"y": [1, 2, 3], "type": "bar"},
            ],
            "layout": {"width": 1000},
        }

        # Compute expected figure dict (pop uids for comparison)
        result = figure.to_dict()

        # Perform comparison
        self.assertEqual(result, expected)

    def test_update_frames(self):
        # Check initial frame axis title
        self.assertEqual(self.figure.frames[0].layout.yaxis.title.text, "f1")

        # Update with dict kwarg
        self.figure.update(frames={0: {"layout": {"yaxis": {"title": {"text": "f2"}}}}})
        self.assertEqual(self.figure.frames[0].layout.yaxis.title.text, "f2")

        # Update with list kwarg
        self.figure.update(frames=[{"layout": {"yaxis": {"title": {"text": "f3"}}}}])
        self.assertEqual(self.figure.frames[0].layout.yaxis.title.text, "f3")

        # Update with dict
        self.figure.update(
            {"frames": [{"layout": {"yaxis": {"title": {"text": "f4"}}}}]}
        )
        self.assertEqual(self.figure.frames[0].layout.yaxis.title.text, "f4")

    def test_update_invalid_attr(self):
        with pytest.raises(ValueError):
            self.figure.layout.update({"xaxis": {"bogus": 32}})

    # plotly_restyle
    def test_plotly_restyle(self):
        # Check initial marker color
        self.assertEqual(self.figure.data[0].marker.color, "green")

        # Update with dict kwarg
        self.figure.plotly_restyle(
            restyle_data={"marker.color": "blue"}, trace_indexes=0
        )

        self.assertEqual(self.figure.data[0].marker.color, "blue")

    def test_restyle_validate_property(self):
        with pytest.raises(ValueError):
            self.figure.plotly_restyle({"bogus": 3}, trace_indexes=[0])

    def test_restyle_validate_property_nested(self):
        with pytest.raises(ValueError):
            self.figure.plotly_restyle({"marker.bogus": 3}, trace_indexes=[0])

    # plotly_relayout
    def test_plotly_relayout(self):
        # Check initial x-range
        self.assertEqual(self.figure.layout.xaxis.range, (-1, 4))

        # Update with kwarg
        self.figure.plotly_relayout(relayout_data={"xaxis.range": [10, 20]})
        self.assertEqual(self.figure.layout.xaxis.range, (10, 20))

    def test_relayout_validate_property(self):
        with pytest.raises(ValueError):
            self.figure.plotly_relayout({"bogus": [1, 3]})

    def test_relayout_validate_property_nested(self):
        with pytest.raises(ValueError):
            self.figure.plotly_relayout({"xaxis.bogus": [1, 3]})

    def test_relayout_validate_unintialized_subplot(self):
        with pytest.raises(ValueError):
            self.figure.plotly_relayout({"xaxis2.range": [1, 3]})

    # plotly_update
    def test_plotly_update_layout(self):
        # Check initial x-range
        self.assertEqual(self.figure.layout.xaxis.range, (-1, 4))

        # Update with kwarg
        self.figure.plotly_update(relayout_data={"xaxis.range": [10, 20]})
        self.assertEqual(self.figure.layout.xaxis.range, (10, 20))

    def test_plotly_update_data(self):
        # Check initial marker color
        self.assertEqual(self.figure.data[0].marker.color, "green")

        # Update with dict kwarg
        self.figure.plotly_update(
            restyle_data={"marker.color": "blue"}, trace_indexes=0
        )

        self.assertEqual(self.figure.data[0].marker.color, "blue")

    def test_plotly_update_validate_property_trace(self):
        with pytest.raises(ValueError):
            self.figure.plotly_update(restyle_data={"bogus": 3}, trace_indexes=[0])

    def test_plotly_update_validate_property_layout(self):
        with pytest.raises(ValueError):
            self.figure.plotly_update(relayout_data={"xaxis.bogus": [1, 3]})
