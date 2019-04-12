from unittest import TestCase

from nose.tools import raises
import plotly.tools as tls
from plotly.exceptions import PlotlyError
import plotly.colors as colors


class TestColors(TestCase):

    def test_validate_colors(self):

        # test string input
        color_string = 'foo'

        pattern = ("If your colors variable is a string, it must be a "
                   "Plotly scale, an rgb color or a hex color.")

        self.assertRaisesRegexp(PlotlyError, pattern, colors.validate_colors,
                                color_string)

        # test rgb color
        color_string2 = 'rgb(265, 0, 0)'

        pattern2 = ("Whoops! The elements in your rgb colors tuples cannot "
                    "exceed 255.0.")

        self.assertRaisesRegexp(PlotlyError, pattern2, colors.validate_colors,
                                color_string2)

        # test tuple color
        color_tuple = (1, 1, 2)

        pattern3 = ("Whoops! The elements in your colors tuples cannot "
                    "exceed 1.0.")

        self.assertRaisesRegexp(PlotlyError, pattern3, colors.validate_colors,
                                color_tuple)

    def test_convert_colors_to_same_type(self):

        # test colortype
        color_tuple = ['#aaaaaa', '#bbbbbb', '#cccccc']
        scale = [0, 1]

        self.assertRaises(PlotlyError, colors.convert_colors_to_same_type,
                          color_tuple, scale=scale)

        # test colortype
        color_tuple = (1, 1, 1)
        colortype = 2

        pattern2 = ("You must select either rgb or tuple for your colortype "
                    "variable.")

        self.assertRaisesRegexp(PlotlyError, pattern2,
                                colors.convert_colors_to_same_type,
                                color_tuple, colortype)

    def test_convert_dict_colors_to_same_type(self):

        # test colortype
        color_dict = dict(apple='rgb(1, 1, 1)')
        colortype = 2

        pattern = ("You must select either rgb or tuple for your colortype "
                   "variable.")

        self.assertRaisesRegexp(PlotlyError, pattern,
                                colors.convert_dict_colors_to_same_type,
                                color_dict, colortype)

    def test_validate_scale_values(self):

        # test that scale length is at least 2
        scale = [0]

        pattern = ("You must input a list of scale values that has at least "
                   "two values.")

        self.assertRaisesRegexp(PlotlyError, pattern,
                                colors.validate_scale_values,
                                scale)

        # test if first and last number is 0 and 1 respectively
        scale = [0, 1.1]

        pattern = ("The first and last number in your scale must be 0.0 and "
                   "1.0 respectively.")

        self.assertRaisesRegexp(PlotlyError, pattern,
                                colors.validate_scale_values,
                                scale)

        # test numbers increase
        scale = [0, 2, 1]

        pattern = ("'scale' must be a list that contains a strictly "
                   "increasing sequence of numbers.")

        self.assertRaisesRegexp(PlotlyError, pattern,
                                colors.validate_scale_values,
                                scale)

    def test_make_colorscale(self):

        # test minimum colors length
        color_list = [(0, 0, 0)]

        pattern = (
            "You must input a list of colors that has at least two colors."
        )

        self.assertRaisesRegexp(PlotlyError, pattern, colors.make_colorscale,
                                color_list)

        # test length of colors and scale
        color_list2 = [(0, 0, 0), (1, 1, 1)]
        scale = [0]

        pattern2 = ("The length of colors and scale must be the same.")

        self.assertRaisesRegexp(PlotlyError, pattern2, colors.make_colorscale,
                                color_list2, scale)
