import math
from unittest import TestCase

from nose.tools import raises
import plotly.tools as tls
from plotly.exceptions import PlotlyError
import plotly.colors as colors

"""
class TestColors(TestCase):

    def test_validate_colors(self):

        # test string input
        color = 'foo'

        pattern = ("If your colors variable is a string, it must be a "
                   "Plotly scale, an rgb color or a hex color.")

        self.assertRaisesRegexp(PlotlyError, pattern, colors.validate_colors,
                                color)

        # test rgb color
        color2 = 'rgb(265,0,0)'

        pattern2 = ("Whoops! The elements in your rgb colors tuples cannot "
                    "exceed 255.0.")

        self.assertRaisesRegexp(PlotlyError, pattern2, colors.validate_colors,
                                color2)

        # test tuple color

        color3 = (1.1, 1, 1)

        pattern3 = ("Whoops! The elements in your colors tuples cannot "
                    "exceed 1.0.")

        self.assertRaisesRegexp(PlotlyError, pattern3, colors.validate_colors,
                                color3)
"""