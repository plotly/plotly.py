"""
Module to test plotly.utils with optional dependencies.

"""
from __future__ import absolute_import

from unittest import TestCase
from plotly.exceptions import PlotlyError

import plotly.figure_factory.utils as utils

import pandas as pd


class TestFigureFactoryUtils(TestCase):

    def test_validate_index(self):
        pattern = (
            "Error in indexing column. "
            "Make sure all entries of each "
            "column are all numbers or "
            "all strings."
        )

        index = [1, 'b', 3]
        index_series = pd.Series([1, 'a', 3], index=[7, 3, 7])

        self.assertRaisesRegexp(PlotlyError, pattern,
                                utils.validate_index, index)

        self.assertRaisesRegexp(PlotlyError, pattern,
                                utils.validate_index, index_series)

    def test_validate_dataframe(self):
        pattern = (
            "Error in dataframe. "
            "Make sure all entries of "
            "each column are either "
            "numbers or strings."
        )

        df1 = [[1, 'b', 3], ['a', 2, 'c']]
        df2 = pd.DataFrame(df1, index=[3, 4])

        self.assertRaisesRegexp(PlotlyError, pattern,
                                utils.validate_dataframe, df1)

        self.assertRaisesRegexp(PlotlyError, pattern,
                                utils.validate_dataframe, df2)


# TODO: transfer all tests from test_optional/test_tools/test_figurefactory.py
# and test_optional/test_figurefactory/test_figurefactory.py to this module
