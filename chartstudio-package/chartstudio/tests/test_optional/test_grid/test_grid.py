"""
test_grid:
==========

A module intended for use with Nose.

"""
from __future__ import absolute_import

from unittest import TestCase

from chartstudio.exceptions import InputError
from chartstudio.grid_objs import Grid

import pandas as pd


class TestDataframeToGrid(TestCase):

    # Test duplicate columns
    def test_duplicate_columns(self):
        df = pd.DataFrame([[1, 'a'], [2, 'b']],
                          columns=['col_1', 'col_1'])

        expected_message = (
            "Yikes, plotly grids currently "
            "can't have duplicate column names. Rename "
            "the column \"{}\" and try again.".format('col_1')
        )

        with self.assertRaisesRegexp(InputError, expected_message):
            Grid(df)
