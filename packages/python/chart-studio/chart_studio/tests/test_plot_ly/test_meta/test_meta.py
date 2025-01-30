"""
test_meta:
==========

A module intended for use with Nose.

"""


import random
import string

from unittest import skip

from chart_studio import plotly as py
from chart_studio.exceptions import PlotlyRequestError
from chart_studio.grid_objs import Column, Grid
from chart_studio.tests.utils import PlotlyTestCase


class MetaTest(PlotlyTestCase):

    _grid = grid = Grid([Column([1, 2, 3, 4], "first column")])
    _meta = {"settings": {"scope1": {"model": "Unicorn Finder", "voltage": 4}}}

    def setUp(self):
        super(MetaTest, self).setUp()
        py.sign_in("PythonTest", "xnyU0DEwvAQQCwHVseIL")

    def random_filename(self):
        random_chars = [random.choice(string.ascii_uppercase) for _ in range(5)]
        unique_filename = "Valid Grid with Meta " + "".join(random_chars)
        return unique_filename

    def test_upload_meta(self):
        unique_filename = self.random_filename()
        grid_url = py.grid_ops.upload(self._grid, unique_filename, auto_open=False)

        # Add some Metadata to that grid
        py.meta_ops.upload(self._meta, grid_url=grid_url)

    def test_upload_meta_with_grid(self):
        c1 = Column([1, 2, 3, 4], "first column")
        Grid([c1])

        unique_filename = self.random_filename()

        py.grid_ops.upload(
            self._grid, unique_filename, meta=self._meta, auto_open=False
        )

    @skip(
        "adding this for now so test_file_tools pass, more info"
        + "https://github.com/plotly/python-api/issues/263"
    )
    def test_metadata_to_nonexistent_grid(self):
        non_exist_meta_url = "https://local.plotly.com/~GridTest/999999999"
        with self.assertRaises(PlotlyRequestError):
            py.meta_ops.upload(self._meta, grid_url=non_exist_meta_url)
