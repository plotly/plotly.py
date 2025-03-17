from unittest import TestCase
import pytest

import plotly.graph_objs as go
import plotly.io as pio


class TestLayoutSubplots(TestCase):
    def setUp(self):
        # Construct initial scatter object
        self.layout = go.Layout()

        pio.templates.default = None

    def tearDown(self):
        pio.templates.default = "plotly"

    def test_initial_access_subplots(self):

        # It should be possible to access base subplots initially
        self.assertEqual(self.layout.xaxis, go.layout.XAxis())
        self.assertEqual(self.layout.yaxis, go.layout.YAxis())
        self.assertEqual(self.layout["geo"], go.layout.Geo())
        self.assertEqual(self.layout.scene, go.layout.Scene())
        self.assertEqual(self.layout.mapbox, go.layout.Mapbox())
        self.assertEqual(self.layout.polar, go.layout.Polar())

        # Subplot ids of 1 should be mapped to the same object as the base
        # subplot. Notice we're using assertIs not assertEqual here
        self.assertIs(self.layout.xaxis, self.layout.xaxis1)
        self.assertIs(self.layout.yaxis, self.layout.yaxis1)
        self.assertIs(self.layout.geo, self.layout.geo1)
        self.assertIs(self.layout.scene, self.layout.scene1)
        self.assertIs(self.layout.mapbox, self.layout.mapbox1)
        self.assertIs(self.layout.polar, self.layout.polar1)

    def test_initial_access_subplot2(self):
        with pytest.raises(AttributeError):
            self.layout.xaxis2

    def test_initial_access_subplot2(self):
        with pytest.raises(KeyError):
            self.layout["xaxis2"]

    def test_assign_subplots(self):
        self.assertIsNone(self.layout.xaxis.title.text)
        self.assertIsNone(self.layout.xaxis1.title.text)

        title_str = "xaxis title"
        self.layout.xaxis.title.text = title_str
        self.assertEqual(self.layout.xaxis.title.text, title_str)
        self.assertEqual(self.layout.xaxis1.title.text, title_str)

    def test_assign_subplot2(self):
        # Init xaxis2
        self.layout.xaxis2 = go.layout.XAxis()

        # Properties are initially None
        self.assertIsNone(self.layout.xaxis2.range)

        # Set range
        xrange = [0, 1]
        self.layout.xaxis2.range = [0, 1]
        self.assertEqual(self.layout.xaxis2.range, tuple(xrange))

        # Make sure range isn't shared with xaxis, or xaxis1
        self.assertIsNone(self.layout.xaxis.range)
        self.assertIsNone(self.layout.xaxis1.range)

    def test_contains(self):

        # Initially xaxis and xaxis1 are `in` layout, but xaxis2 and 3 are not
        self.assertTrue("xaxis" in self.layout)
        self.assertTrue("xaxis1" in self.layout)
        self.assertFalse("xaxis2" in self.layout)
        self.assertFalse("xaxis3" in self.layout)

        # xaxis is in iter props, but xaxis1, 2, and 3 are not
        iter_props = list(self.layout)
        self.assertIn("xaxis", iter_props)
        self.assertNotIn("xaxis1", iter_props)
        self.assertNotIn("xaxis2", iter_props)
        self.assertNotIn("xaxis3", iter_props)

        # test dir props (these drive ipython tab completion)
        dir_props = self.layout.__dir__()
        self.assertIn("xaxis", dir_props)
        self.assertNotIn("xaxis1", dir_props)
        self.assertNotIn("xaxis2", dir_props)
        self.assertNotIn("xaxis3", dir_props)

        # Initialize xaxis2
        self.layout.xaxis2 = {}
        self.assertTrue("xaxis" in self.layout)
        self.assertTrue("xaxis1" in self.layout)
        self.assertTrue("xaxis2" in self.layout)
        self.assertFalse("xaxis3" in self.layout)

        # xaxis and xaxis2 are in iter props
        iter_props = list(self.layout)
        self.assertIn("xaxis", iter_props)
        self.assertNotIn("xaxis1", iter_props)
        self.assertIn("xaxis2", iter_props)
        self.assertNotIn("xaxis3", iter_props)

        # test dir props
        dir_props = self.layout.__dir__()
        self.assertIn("xaxis", dir_props)
        self.assertNotIn("xaxis1", dir_props)
        self.assertIn("xaxis2", dir_props)
        self.assertNotIn("xaxis3", dir_props)

        # Initialize xaxis3
        self.layout["xaxis3"] = {}
        self.assertTrue("xaxis" in self.layout)
        self.assertTrue("xaxis1" in self.layout)
        self.assertTrue("xaxis2" in self.layout)
        self.assertTrue("xaxis3" in self.layout)

        # xaxis, xaxis2, and xaxis3 are in iter props
        iter_props = list(self.layout)
        self.assertIn("xaxis", iter_props)
        self.assertNotIn("xaxis1", iter_props)
        self.assertIn("xaxis2", iter_props)
        self.assertIn("xaxis3", iter_props)

        # test dir props
        dir_props = self.layout.__dir__()
        self.assertIn("xaxis", dir_props)
        self.assertNotIn("xaxis1", dir_props)
        self.assertIn("xaxis2", dir_props)
        self.assertIn("xaxis3", dir_props)

    def test_subplot_objs_have_proper_type(self):
        self.layout.xaxis2 = {}
        self.assertIsInstance(self.layout.xaxis2, go.layout.XAxis)

        self.layout.yaxis3 = {}
        self.assertIsInstance(self.layout.yaxis3, go.layout.YAxis)

        self.layout.geo4 = {}
        self.assertIsInstance(self.layout.geo4, go.layout.Geo)

        self.layout.ternary5 = {}
        self.assertIsInstance(self.layout.ternary5, go.layout.Ternary)

        self.layout.scene6 = {}
        self.assertIsInstance(self.layout.scene6, go.layout.Scene)

        self.layout.mapbox7 = {}
        self.assertIsInstance(self.layout.mapbox7, go.layout.Mapbox)

        self.layout.polar8 = {}
        self.assertIsInstance(self.layout.polar8, go.layout.Polar)

    def test_subplot_1_in_constructor(self):
        layout = go.Layout(xaxis1=go.layout.XAxis(title={"text": "xaxis 1"}))
        self.assertEqual(layout.xaxis1.title.text, "xaxis 1")

    def test_subplot_props_in_constructor(self):
        layout = go.Layout(
            xaxis2=go.layout.XAxis(title={"text": "xaxis 2"}),
            yaxis3=go.layout.YAxis(title={"text": "yaxis 3"}),
            geo4=go.layout.Geo(bgcolor="blue"),
            ternary5=go.layout.Ternary(sum=120),
            scene6=go.layout.Scene(dragmode="zoom"),
            mapbox7=go.layout.Mapbox(zoom=2),
            polar8=go.layout.Polar(sector=[0, 90]),
        )

        self.assertEqual(layout.xaxis2.title.text, "xaxis 2")
        self.assertEqual(layout.yaxis3.title.text, "yaxis 3")
        self.assertEqual(layout.geo4.bgcolor, "blue")
        self.assertEqual(layout.ternary5.sum, 120)
        self.assertEqual(layout.scene6.dragmode, "zoom")
        self.assertEqual(layout.mapbox7.zoom, 2)
        self.assertEqual(layout.polar8.sector, (0, 90))

    def test_create_subplot_with_update(self):

        self.layout.update(
            xaxis1=go.layout.XAxis(title={"text": "xaxis 1"}),
            xaxis2=go.layout.XAxis(title={"text": "xaxis 2"}),
            yaxis3=go.layout.YAxis(title={"text": "yaxis 3"}),
            geo4=go.layout.Geo(bgcolor="blue"),
            ternary5=go.layout.Ternary(sum=120),
            scene6=go.layout.Scene(dragmode="zoom"),
            mapbox7=go.layout.Mapbox(zoom=2),
            polar8=go.layout.Polar(sector=[0, 90]),
        )

        self.assertEqual(self.layout.xaxis1.title.text, "xaxis 1")
        self.assertEqual(self.layout.xaxis2.title.text, "xaxis 2")
        self.assertEqual(self.layout.yaxis3.title.text, "yaxis 3")
        self.assertEqual(self.layout.geo4.bgcolor, "blue")
        self.assertEqual(self.layout.ternary5.sum, 120)
        self.assertEqual(self.layout.scene6.dragmode, "zoom")
        self.assertEqual(self.layout.mapbox7.zoom, 2)
        self.assertEqual(self.layout.polar8.sector, (0, 90))

    def test_create_subplot_with_update_dict(self):

        self.layout.update(
            {
                "xaxis1": {"title": {"text": "xaxis 1"}},
                "xaxis2": {"title": {"text": "xaxis 2"}},
                "yaxis3": {"title": {"text": "yaxis 3"}},
                "geo4": {"bgcolor": "blue"},
                "ternary5": {"sum": 120},
                "scene6": {"dragmode": "zoom"},
                "mapbox7": {"zoom": 2},
                "polar8": {"sector": [0, 90]},
            }
        )

        self.assertEqual(self.layout.xaxis1.title.text, "xaxis 1")
        self.assertEqual(self.layout.xaxis2.title.text, "xaxis 2")
        self.assertEqual(self.layout.yaxis3.title.text, "yaxis 3")
        self.assertEqual(self.layout.geo4.bgcolor, "blue")
        self.assertEqual(self.layout.ternary5.sum, 120)
        self.assertEqual(self.layout.scene6.dragmode, "zoom")
        self.assertEqual(self.layout.mapbox7.zoom, 2)
        self.assertEqual(self.layout.polar8.sector, (0, 90))

    def test_bug_1462(self):
        # https: // github.com / plotly / plotly.py / issues / 1462
        fig = go.Figure(
            data=[
                go.Scatter(x=[1, 2], y=[1, 2], xaxis="x"),
                go.Scatter(x=[2, 3], y=[2, 3], xaxis="x2"),
            ]
        )

        layout_dict = {
            "grid": {"xaxes": ["x", "x2"], "yaxes": ["y"]},
            "xaxis2": {"matches": "x", "title": {"text": "total_bill"}},
        }

        fig.update(layout=layout_dict)
        updated_layout_dict = fig.layout.to_plotly_json()

        self.assertEqual(updated_layout_dict, layout_dict)
