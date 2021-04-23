from unittest import TestCase

import plotly.graph_objs as go


OLD_CLASS_NAMES = [
    "AngularAxis",
    "Annotation",
    "Annotations",
    "Bar",
    "Box",
    "ColorBar",
    "Contour",
    "Contours",
    "Data",
    "ErrorX",
    "ErrorY",
    "ErrorZ",
    "Figure",
    "Font",
    "Frame",
    "Frames",
    "Heatmap",
    "Histogram",
    "Histogram2d",
    "Histogram2dContour",
    "Layout",
    "Legend",
    "Line",
    "Margin",
    "Marker",
    "RadialAxis",
    "Scatter",
    "Scatter3d",
    "Scene",
    "Stream",
    "Surface",
    "Trace",
    "XAxis",
    "XBins",
    "YAxis",
    "YBins",
    "ZAxis",
]


class TestBackwardsCompat(TestCase):
    def test_old_class_names(self):

        # these were all defined at one point, we want to maintain backwards
        # compat, so we basically just create a checkpoint with this test.

        for class_name in OLD_CLASS_NAMES:
            self.assertIsNotNone(getattr(go, class_name, None))

    def test_title_as_string_layout(self):
        """
        Prior to plotly.js 1.43.0 title properties were strings, in 1.43.0
        these title properties became compound objects with a text property.

        For backwards compatibility, we still need to support setting this
        title object as a string or number
        """
        layout_title_parents = [
            go.Layout(),
            go.layout.XAxis(),
            go.layout.YAxis(),
            go.layout.ternary.Aaxis(),
            go.layout.ternary.Baxis(),
            go.layout.ternary.Caxis(),
            go.layout.scene.XAxis(),
            go.layout.scene.YAxis(),
            go.layout.scene.ZAxis(),
            go.layout.polar.RadialAxis(),
            go.scatter.marker.ColorBar(),
            go.cone.ColorBar(),
        ]

        for obj in layout_title_parents:
            obj.title = "A title"

            self.assertEqual(obj.title.text, "A title")
            self.assertEqual(obj.to_plotly_json(), {"title": {"text": "A title"}})

            # And update
            obj.update(title="A title 2")
            self.assertEqual(obj.title.text, "A title 2")
            self.assertEqual(obj.to_plotly_json(), {"title": {"text": "A title 2"}})

            # Update titlefont
            obj.update(titlefont={"size": 23})
            self.assertEqual(obj.title.font.size, 23)
            self.assertEqual(
                obj.to_plotly_json(),
                {"title": {"text": "A title 2", "font": {"size": 23}}},
            )

        # Pie
        obj = go.Pie()
        obj.title = "A title"
        self.assertEqual(obj.title.text, "A title")
        self.assertEqual(
            obj.to_plotly_json(), {"title": {"text": "A title"}, "type": "pie"}
        )

        # And update
        obj.update(title="A title 2")
        self.assertEqual(obj.title.text, "A title 2")
        self.assertEqual(
            obj.to_plotly_json(), {"type": "pie", "title": {"text": "A title 2"}}
        )

        # Update titlefont
        obj.update(titlefont={"size": 23})
        self.assertEqual(obj.title.font.size, 23)
        self.assertEqual(
            obj.to_plotly_json(),
            {"type": "pie", "title": {"text": "A title 2", "font": {"size": 23}}},
        )

    def test_legacy_title_props_remapped(self):

        # plain Layout
        obj = go.Layout()
        self.assertIs(obj.titlefont, obj.title.font)
        self.assertIsNone(obj.title.font.family)

        # Set titlefont in constructor
        obj = go.Layout(titlefont={"family": "Courier"})
        self.assertIs(obj.titlefont, obj.title.font)
        self.assertEqual(obj.titlefont.family, "Courier")
        self.assertEqual(obj.title.font.family, "Courier")

        # Property assignment
        obj = go.Layout()
        obj.titlefont.family = "Courier"
        self.assertIs(obj.titlefont, obj.title.font)
        self.assertEqual(obj["titlefont.family"], "Courier")
        self.assertEqual(obj.title.font.family, "Courier")

        # In/Iter
        self.assertIn("titlefont", obj)
        self.assertIn("titlefont.family", obj)
        self.assertIn("titlefont", iter(obj))


class TestPop(TestCase):
    def setUp(self):
        self.layout = go.Layout(
            width=1000,
            title={"text": "the title", "font": {"size": 20}},
            annotations=[{}, {}],
            xaxis2={"range": [1, 2]},
        )

    def test_pop_valid_simple_prop(self):
        self.assertEqual(self.layout.width, 1000)
        self.assertEqual(self.layout.pop("width"), 1000)
        self.assertIsNone(self.layout.width)

    def test_pop_valid_compound_prop(self):
        val = self.layout.title
        self.assertEqual(self.layout.pop("title"), val)
        self.assertEqual(self.layout.title, go.layout.Title())

    def test_pop_valid_array_prop(self):
        val = self.layout.annotations
        self.assertEqual(self.layout.pop("annotations"), val)
        self.assertEqual(self.layout.annotations, ())

    def test_pop_valid_subplot_prop(self):
        val = self.layout.xaxis2
        self.assertEqual(self.layout.pop("xaxis2"), val)
        self.assertEqual(self.layout.xaxis2, go.layout.XAxis())

    def test_pop_invalid_prop_key_error(self):
        with self.assertRaises(KeyError):
            self.layout.pop("bogus")

    def test_pop_invalid_prop_with_default(self):
        self.assertEqual(self.layout.pop("bogus", 42), 42)
