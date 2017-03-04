"""
test_meta:
==========

A module intended for use with Nose.

"""
from __future__ import absolute_import

import random
import string

from nose.plugins.attrib import attr
from unittest import skip

import plotly.plotly as py
from plotly.exceptions import PlotlyRequestError
from plotly.grid_objs import Column, Grid
from plotly.tests.utils import PlotlyTestCase


class MetaTest(PlotlyTestCase):

    _grid = grid = Grid([Column([1, 2, 3, 4], 'first column')])
    _meta = {"settings": {"scope1": {"model": "Unicorn Finder", "voltage": 4}}}

    def setUp(self):
        super(MetaTest, self).setUp()
        py.sign_in('PythonTest', '9v9f20pext')

    def random_filename(self):
        random_chars = [random.choice(string.ascii_uppercase) for _ in range(5)]
        unique_filename = 'Valid Grid with Meta '+''.join(random_chars)
        return unique_filename

    @attr('slow')
    def test_upload_meta(self):
        unique_filename = self.random_filename()
        grid_url = py.grid_ops.upload(self._grid, unique_filename,
                                      auto_open=False)

        # Add some Metadata to that grid
        py.meta_ops.upload(self._meta, grid_url=grid_url)

    @attr('slow')
    def test_upload_meta_with_grid(self):
        c1 = Column([1, 2, 3, 4], 'first column')
        Grid([c1])

        unique_filename = self.random_filename()

        py.grid_ops.upload(
            self._grid,
            unique_filename,
            meta=self._meta,
            auto_open=False)

    @skip('adding this for now so test_file_tools pass, more info' +
          'https://github.com/plotly/python-api/issues/263')
    def test_metadata_to_nonexistent_grid(self):
        non_exist_meta_url = 'https://local.plot.ly/~GridTest/999999999'
        with self.assertRaises(PlotlyRequestError):
            py.meta_ops.upload(self._meta, grid_url=non_exist_meta_url)
