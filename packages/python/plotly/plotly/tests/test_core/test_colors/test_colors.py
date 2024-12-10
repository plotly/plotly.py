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

        self.assertRaisesRegex(
            PlotlyError, pattern, colors.validate_colors, color_string
        )

        # test rgb color
        color_string2 = "rgb(265, 0, 0)"

        pattern2 = (
            "Whoops! The elements in your rgb colors tuples cannot " "exceed 255.0."
        )

        self.assertRaisesRegex(
            PlotlyError, pattern2, colors.validate_colors, color_string2
        )

        # test tuple color
        color_tuple = (1, 1, 2)

        pattern3 = "Whoops! The elements in your colors tuples cannot " "exceed 1.0."

        self.assertRaisesRegex(
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

        self.assertRaisesRegex(
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

        self.assertRaisesRegex(
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

        self.assertRaisesRegex(
            PlotlyError, pattern, colors.validate_scale_values, scale
        )

        # test if first and last number is 0 and 1 respectively
        scale = [0, 1.1]

        pattern = (
            "The first and last number in your scale must be 0.0 and "
            "1.0 respectively."
        )

        self.assertRaisesRegex(
            PlotlyError, pattern, colors.validate_scale_values, scale
        )

        # test numbers increase
        scale = [0, 2, 1]

        pattern = (
            "'scale' must be a list that contains a strictly "
            "increasing sequence of numbers."
        )

        self.assertRaisesRegex(
            PlotlyError, pattern, colors.validate_scale_values, scale
        )

    def test_make_colorscale(self):

        # test minimum colors length
        color_list = [(0, 0, 0)]

        pattern = "You must input a list of colors that has at least two colors."

        self.assertRaisesRegex(PlotlyError, pattern, colors.make_colorscale, color_list)

        # test length of colors and scale
        color_list2 = [(0, 0, 0), (1, 1, 1)]
        scale = [0]

        pattern2 = "The length of colors and scale must be the same."

        self.assertRaisesRegex(
            PlotlyError, pattern2, colors.make_colorscale, color_list2, scale
        )

    def test_get_colorscale(self):

        # test for incorrect input type
        pattern = "Name argument have to be a string."
        name = colors.sequential.haline

        self.assertRaisesRegex(PlotlyError, pattern, colors.get_colorscale, name)

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
            colors.sample_colorscale("TuRbId_r", 12),
            colors.sequential.turbid_r,
        )

    def test_n_colors(self):
        # test that n_colors constrains values to between 0 and 255
        generated_colorscale = colors.n_colors(
            lowcolor="rgb(255,0,0)",
            highcolor="rgb(0,255,0)",
            n_colors=14,
            colortype="rgb",
        )
        expected_colorscale = [
            "rgb(255.0, 0.0, 0.0)",
            "rgb(235.3846153846154, 19.615384615384617, 0.0)",
            "rgb(215.76923076923077, 39.23076923076923, 0.0)",
            "rgb(196.15384615384613, 58.846153846153854, 0.0)",
            "rgb(176.53846153846155, 78.46153846153847, 0.0)",
            "rgb(156.9230769230769, 98.07692307692308, 0.0)",
            "rgb(137.3076923076923, 117.69230769230771, 0.0)",
            "rgb(117.69230769230768, 137.30769230769232, 0.0)",
            "rgb(98.07692307692307, 156.92307692307693, 0.0)",
            "rgb(78.46153846153845, 176.53846153846155, 0.0)",
            "rgb(58.84615384615384, 196.15384615384616, 0.0)",
            "rgb(39.230769230769226, 215.76923076923077, 0.0)",
            "rgb(19.615384615384585, 235.38461538461542, 0.0)",
            "rgb(0.0, 255.0, 0.0)",
        ]

        self.assertEqual(generated_colorscale, expected_colorscale)
