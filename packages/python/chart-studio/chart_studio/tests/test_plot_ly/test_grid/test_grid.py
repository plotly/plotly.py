"""
test_grid:
==========

A module intended for use with Nose.

"""


import random
import string
from unittest import skip


from chart_studio import plotly as py
from chart_studio.exceptions import InputError, PlotlyRequestError
from _plotly_utils.exceptions import PlotlyError
from plotly.graph_objs import Scatter
from chart_studio.grid_objs import Column, Grid
from chart_studio.plotly import parse_grid_id_args
from chart_studio.tests.utils import PlotlyTestCase


def random_filename():
    choice_chars = string.ascii_letters + string.digits
    random_chars = [random.choice(choice_chars) for _ in range(10)]
    unique_filename = "Valid Grid " + "".join(random_chars)
    return unique_filename


class GridTest(PlotlyTestCase):

    # Test grid args
    _grid_id = "chris:3043"
    _grid = Grid([])
    _grid.id = _grid_id
    _grid_url = "https://plotly.com/~chris/3043/my-grid"

    def setUp(self):
        super(GridTest, self).setUp()
        py.sign_in("PythonTest", "xnyU0DEwvAQQCwHVseIL")

    def get_grid(self):
        c1 = Column([1, 2, 3, 4], "first column")
        c2 = Column(["a", "b", "c", "d"], "second column")
        g = Grid([c1, c2])
        return g

    def upload_and_return_grid(self):
        g = self.get_grid()
        unique_filename = random_filename()
        py.grid_ops.upload(g, unique_filename, auto_open=False)
        return g

    # Nominal usage
    def test_grid_upload(self):
        self.upload_and_return_grid()

    def test_grid_upload_in_new_folder(self):
        g = self.get_grid()
        path = "new folder: {0}/grid in folder {1}".format(
            random_filename(), random_filename()
        )
        py.grid_ops.upload(g, path, auto_open=False)

    def test_grid_upload_in_existing_folder(self):
        g = self.get_grid()
        folder = random_filename()
        filename = random_filename()
        py.file_ops.mkdirs(folder)
        path = "existing folder: {0}/grid in folder {1}".format(folder, filename)
        py.grid_ops.upload(g, path, auto_open=False)

    def test_column_append(self):
        g = self.upload_and_return_grid()
        new_col = Column([1, 5, 3], "new col")
        py.grid_ops.append_columns([new_col], grid=g)

    def test_row_append(self):
        g = self.upload_and_return_grid()
        new_rows = [[1, 2], [10, 20]]
        py.grid_ops.append_rows(new_rows, grid=g)

    def test_plot_from_grid(self):
        g = self.upload_and_return_grid()
        url = py.plot(
            [Scatter(xsrc=g[0].id, ysrc=g[1].id)],
            auto_open=False,
            filename="plot from grid",
        )
        return url, g

    def test_get_figure_from_references(self):
        url, g = self.test_plot_from_grid()
        fig = py.get_figure(url)
        data = fig["data"]
        trace = data[0]
        assert tuple(g[0].data) == tuple(trace["x"])
        assert tuple(g[1].data) == tuple(trace["y"])

    def test_grid_id_args(self):
        self.assertEqual(
            parse_grid_id_args(self._grid, None),
            parse_grid_id_args(None, self._grid_url),
        )

    def test_no_grid_id_args(self):
        with self.assertRaises(InputError):
            parse_grid_id_args(None, None)

    def test_overspecified_grid_args(self):
        with self.assertRaises(InputError):
            parse_grid_id_args(self._grid, self._grid_url)

    # not broken anymore since plotly 3.0.0
    # def test_scatter_from_non_uploaded_grid(self):
    #     c1 = Column([1, 2, 3, 4], 'first column')
    #     c2 = Column(['a', 'b', 'c', 'd'], 'second column')
    #     g = Grid([c1, c2])
    #     with self.assertRaises(ValueError):
    #         Scatter(xsrc=g[0], ysrc=g[1])

    def test_column_append_of_non_uploaded_grid(self):
        c1 = Column([1, 2, 3, 4], "first column")
        c2 = Column(["a", "b", "c", "d"], "second column")
        g = Grid([c1])
        with self.assertRaises(PlotlyError):
            py.grid_ops.append_columns([c2], grid=g)

    def test_row_append_of_non_uploaded_grid(self):
        c1 = Column([1, 2, 3, 4], "first column")
        rows = [[1], [2]]
        g = Grid([c1])
        with self.assertRaises(PlotlyError):
            py.grid_ops.append_rows(rows, grid=g)

    # Input Errors
    def test_unequal_length_rows(self):
        g = self.upload_and_return_grid()
        rows = [[1, 2], ["to", "many", "cells"]]
        with self.assertRaises(InputError):
            py.grid_ops.append_rows(rows, grid=g)

    # Test duplicate columns
    def test_duplicate_columns(self):
        c1 = Column([1, 2, 3, 4], "first column")
        c2 = Column(["a", "b", "c", "d"], "first column")
        with self.assertRaises(InputError):
            Grid([c1, c2])

    # Test delete
    def test_delete_grid(self):
        g = self.get_grid()
        fn = random_filename()
        py.grid_ops.upload(g, fn, auto_open=False)
        py.grid_ops.delete(g)
        py.grid_ops.upload(g, fn, auto_open=False)

    # Plotly failures
    @skip(
        "adding this for now so test_file_tools pass, more info"
        + "https://github.com/plotly/python-api/issues/262"
    )
    def test_duplicate_filenames(self):
        c1 = Column([1, 2, 3, 4], "first column")
        g = Grid([c1])

        random_chars = [random.choice(string.ascii_uppercase) for _ in range(5)]
        unique_filename = "Valid Grid " + "".join(random_chars)
        py.grid_ops.upload(g, unique_filename, auto_open=False)
        try:
            py.grid_ops.upload(g, unique_filename, auto_open=False)
        except PlotlyRequestError as e:
            pass
        else:
            self.fail("Expected this to fail!")
