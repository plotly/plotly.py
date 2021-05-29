from unittest import TestCase

import plotly.tools as tls
from plotly.exceptions import PlotlyError
import plotly.colors as colors


class TestColors(TestCase):
    def test_validate_colors(self):

        # test string input
        color_string = "foo"

        pattern = (
            "If your colors variable is a string, it must be a "
            "Plotly scale, an rgb color or a hex color."
        )

        self.assertRaisesRegexp(
            PlotlyError, pattern, colors.validate_colors, color_string
        )

        # test rgb color
        color_string2 = "rgb(265, 0, 0)"

        pattern2 = (
            "Whoops! The elements in your rgb colors tuples cannot " "exceed 255.0."
        )

        self.assertRaisesRegexp(
            PlotlyError, pattern2, colors.validate_colors, color_string2
        )

        # test tuple color
        color_tuple = (1, 1, 2)

        pattern3 = "Whoops! The elements in your colors tuples cannot " "exceed 1.0."

        self.assertRaisesRegexp(
            PlotlyError, pattern3, colors.validate_colors, color_tuple
        )

    def test_convert_colors_to_same_type(self):

        # test colortype
        color_tuple = ["#aaaaaa", "#bbbbbb", "#cccccc"]
        scale = [0, 1]

        self.assertRaises(
            PlotlyError, colors.convert_colors_to_same_type, color_tuple, scale=scale
        )

        # test colortype
        color_tuple = (1, 1, 1)
        colortype = 2

        pattern2 = "You must select either rgb or tuple for your colortype " "variable."

        self.assertRaisesRegexp(
            PlotlyError,
            pattern2,
            colors.convert_colors_to_same_type,
            color_tuple,
            colortype,
        )

    def test_convert_dict_colors_to_same_type(self):

        # test colortype
        color_dict = dict(apple="rgb(1, 1, 1)")
        colortype = 2

        pattern = "You must select either rgb or tuple for your colortype " "variable."

        self.assertRaisesRegexp(
            PlotlyError,
            pattern,
            colors.convert_dict_colors_to_same_type,
            color_dict,
            colortype,
        )

    def test_validate_scale_values(self):

        # test that scale length is at least 2
        scale = [0]

        pattern = (
            "You must input a list of scale values that has at least " "two values."
        )

        self.assertRaisesRegexp(
            PlotlyError, pattern, colors.validate_scale_values, scale
        )

        # test if first and last number is 0 and 1 respectively
        scale = [0, 1.1]

        pattern = (
            "The first and last number in your scale must be 0.0 and "
            "1.0 respectively."
        )

        self.assertRaisesRegexp(
            PlotlyError, pattern, colors.validate_scale_values, scale
        )

        # test numbers increase
        scale = [0, 2, 1]

        pattern = (
            "'scale' must be a list that contains a strictly "
            "increasing sequence of numbers."
        )

        self.assertRaisesRegexp(
            PlotlyError, pattern, colors.validate_scale_values, scale
        )

    def test_make_colorscale(self):

        # test minimum colors length
        color_list = [(0, 0, 0)]

        pattern = "You must input a list of colors that has at least two colors."

        self.assertRaisesRegexp(
            PlotlyError, pattern, colors.make_colorscale, color_list
        )

        # test length of colors and scale
        color_list2 = [(0, 0, 0), (1, 1, 1)]
        scale = [0]

        pattern2 = "The length of colors and scale must be the same."

        self.assertRaisesRegexp(
            PlotlyError, pattern2, colors.make_colorscale, color_list2, scale
        )

    def test_get_colorscale(self):

        # test for incorrect input type
        pattern = "Name argument have to be a string."
        name = colors.sequential.haline

        self.assertRaisesRegexp(PlotlyError, pattern, colors.get_colorscale, name)

        # test for non-existing colorscale
        pattern = r"Colorscale \S+ is not a built-in scale."
        name = "foo"
        self.assertRaisesRegex(PlotlyError, pattern, colors.get_colorscale, name)

        # test non-capitalised access
        self.assertEqual(
            colors.make_colorscale(colors.sequential.haline),
            colors.get_colorscale("haline"),
        )
        # test capitalised access
        self.assertEqual(
            colors.make_colorscale(colors.diverging.Earth),
            colors.get_colorscale("Earth"),
        )
        # test accessing non-capitalised scale with capitalised name
        self.assertEqual(
            colors.make_colorscale(colors.cyclical.mrybm),
            colors.get_colorscale("Mrybm"),
        )
        # test accessing capitalised scale with non-capitalised name
        self.assertEqual(
            colors.make_colorscale(colors.sequential.Viridis),
            colors.get_colorscale("viridis"),
        )
        # test accessing reversed scale
        self.assertEqual(
            colors.make_colorscale(colors.diverging.Portland_r),
            colors.get_colorscale("portland_r"),
        )

    def test_sample_colorscale(self):

        # test that sampling a colorscale at the defined points returns the same
        defined_colors = colors.sequential.Inferno
        sampled_colors = colors.sample_colorscale(
            defined_colors, len(defined_colors), colortype="rgb"
        )
        defined_colors_rgb = colors.convert_colors_to_same_type(
            defined_colors, colortype="rgb"
        )[0]
        self.assertEqual(sampled_colors, defined_colors_rgb)

        # test sampling an easy colorscale that goes [red, green, blue]
        defined_colors = ["rgb(255,0,0)", "rgb(0,255,0)", "rgb(0,0,255)"]
        samplepoints = [0.0, 0.125, 0.25, 0.375, 0.5, 0.625, 0.75, 0.875, 1.0]
        expected_output = [
            (1.0, 0.0, 0.0),
            (0.75, 0.25, 0.0),
            (0.5, 0.5, 0.0),
            (0.25, 0.75, 0.0),
            (0.0, 1.0, 0.0),
            (0.0, 0.75, 0.25),
            (0.0, 0.5, 0.5),
            (0.0, 0.25, 0.75),
            (0.0, 0.0, 1.0),
        ]
        output = colors.sample_colorscale(
            defined_colors, samplepoints, colortype="tuple"
        )
        self.assertEqual(expected_output, output)

        self.assertEqual(
            colors.sample_colorscale("TuRbId_r", 12), colors.sequential.turbid_r,
        )
