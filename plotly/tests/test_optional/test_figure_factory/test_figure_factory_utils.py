from unittest import TestCase

from nose.tools import raises
import plotly.figure_factory.utils as utils
import plotly.tools as tls
from plotly.exceptions import PlotlyError


class TestFigureFactoryUtils(TestCase):

    def test_validate_index(self):
        pattern = (
            "Error in indexing column. "
            "Make sure all entries of each "
            "column are all numbers or "
            "all strings."
        )

        self.assertRaisesRegexp(PlotlyError, pattern, utils.validate_index,
                                [13, 'foo'])

        self.assertRaisesRegexp(PlotlyError, pattern, utils.validate_index,
                                ['number', 42])

    def validate_dataframe(self):
        pattern = (
            "Error in dataframe. "
            "Make sure all entries of "
            "each column are either "
            "numbers or strings."
        )

        df = [
            [8, 'foo'],
            ['amazing', 64]
        ]

        self.assertRaisesRegexp(PlotlyError, pattern, utils.validate_index, df)

        df = [
            ['amazing', 64],
            [8, 'foo']
        ]

        self.assertRaisesRegexp(PlotlyError, pattern, utils.validate_index, df)


    def validate_equal_length(self):
        pattern = (
            "Oops! Your data lists or ndarrays should be the same length."
        )

        self.assertRaisesRegexp(PlotlyError, pattern, utils.validate_index,
                                (0,0,0), (0,0,0,0,0))


    def test_validate_positive_scalars(self):
        # only one negative number
        self.assertRaises(ValueError, utils.validate_positive_scalars,
                          number0=1, number1=0.001, number2=-2)

    def test_flatten(self):

        self.assertRaises(
            PlotlyError, utils.flatten,
            array=0
        )

    def test_validate_colors(self):

        # test string input
        color_string = 'foo'

        pattern = ("If your colors variable is a string, it must be a "
                   "Plotly scale, an rgb color or a hex color.")

        self.assertRaisesRegexp(PlotlyError, pattern, utils.validate_colors,
                                color_string)

        # test rgb color
        color_string2 = 'rgb(265, 0, 0)'

        pattern2 = ("Whoops! The elements in your rgb colors tuples cannot "
                    "exceed 255.0.")

        self.assertRaisesRegexp(PlotlyError, pattern2, utils.validate_colors,
                                color_string2)

        # test dictionary
        colors_dict = {
            'apple': 'rgb(300, 0, 0)',
            'pear': (0, 0.5, 1)
        }

        self.assertRaisesRegexp(PlotlyError, pattern2, utils.validate_colors_dict,
                                colors_dict)

        # test tuple color
        color_tuple = (1, 1, 2)

        pattern3 = ("Whoops! The elements in your colors tuples cannot "
                    "exceed 1.0.")

        self.assertRaisesRegexp(PlotlyError, pattern3, utils.validate_colors,
                                color_tuple)

        colors_dict2 = {
            'apple': 'rgb(255, 100, 50)',
            'pear': (0, 0.5, 2)
        }

        self.assertRaisesRegexp(PlotlyError, pattern3, utils.validate_colors_dict,
                                colors_dict2)

    def test_convert_colors_to_same_type(self):

        # test colortype
        color_tuple = ['#aaaaaa', '#bbbbbb', '#cccccc']
        scale = [0, 1]

        self.assertRaises(PlotlyError, utils.convert_colors_to_same_type,
                          color_tuple, scale=scale)

        # test colortype
        color_tuple = (1, 1, 1)
        colortype = 2

        pattern2 = ("You must select either rgb or tuple for your colortype "
                    "variable.")

        self.assertRaisesRegexp(PlotlyError, pattern2,
                                utils.convert_colors_to_same_type,
                                color_tuple, colortype)

    def test_convert_dict_colors_to_same_type(self):

        # test colortype
        color_dict = dict(apple='rgb(1, 1, 1)')
        colortype = 2

        pattern = ("You must select either rgb or tuple for your colortype "
                   "variable.")

        self.assertRaisesRegexp(PlotlyError, pattern,
                                utils.convert_dict_colors_to_same_type,
                                color_dict, colortype)

    def test_validate_scale_values(self):

        # test that scale length is at least 2
        scale = [0]

        pattern = ("You must input a list of scale values that has at least "
                   "two values.")

        self.assertRaisesRegexp(PlotlyError, pattern,
                                utils.validate_scale_values,
                                scale)

        # test if first and last number is 0 and 1 respectively
        scale = [0, 1.1]

        pattern = ("The first and last number in your scale must be 0.0 and "
                   "1.0 respectively.")

        self.assertRaisesRegexp(PlotlyError, pattern,
                                utils.validate_scale_values,
                                scale)

        # test numbers increase
        scale = [0, 2, 1]

        pattern = ("'scale' must be a list that contains a strictly "
                   "increasing sequence of numbers.")

        self.assertRaisesRegexp(PlotlyError, pattern,
                                utils.validate_scale_values,
                                scale)

    def test_make_colorscale(self):

        # test minimum colors length
        color_list = [(0, 0, 0)]

        pattern = (
            "You must input a list of colors that has at least two colors."
        )

        self.assertRaisesRegexp(PlotlyError, pattern, utils.make_colorscale,
                                color_list)

        # test length of colors and scale
        color_list2 = [(0, 0, 0), (1, 1, 1)]
        scale = [0]

        pattern2 = ("The length of colors and scale must be the same.")

        self.assertRaisesRegexp(PlotlyError, pattern2, utils.make_colorscale,
                                color_list2, scale)


    def test_endpts_to_intervals(self):

        pattern = ("The intervals_endpts argument must "
                   "be a list or tuple of a sequence "
                   "of increasing numbers.")

        endpts = 'foo'
        self.assertRaisesRegexp(PlotlyError, pattern,
                                utils.endpts_to_intervals, endpts)

        endpts = ['foo']
        self.assertRaisesRegexp(PlotlyError, pattern,
                                utils.endpts_to_intervals, endpts)

        endpts = [1, 0]
        self.assertRaisesRegexp(PlotlyError, pattern,
                                utils.endpts_to_intervals, endpts)

    def test_validate_colorscale(self):

        pattern = "A valid colorscale must be a list."

        colorscale = 55
        self.assertRaisesRegexp(PlotlyError, pattern,
                                utils.validate_colorscale, colorscale)

        pattern2 = "A valid colorscale must be a list of lists."

        colorscale = [[], [], 'foo', []]
        self.assertRaisesRegexp(PlotlyError, pattern,
                                utils.validate_colorscale, colorscale)
        
    def test_list_of_options(self):

        pattern = 'Your list or tuple must contain at least 2 items.'

        self.assertRaisesRegexp(PlotlyError, pattern,
                                utils.list_of_options, ['item #1'])





