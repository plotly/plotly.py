"""
test_grid:
==========

A module intended for use with Nose.

"""
from __future__ import absolute_import

import random
import string
import requests

from nose import with_setup
from nose.plugins.attrib import attr
from nose.tools import raises
from unittest import skip

import plotly.plotly as py
from plotly.exceptions import InputError, PlotlyRequestError
from plotly.graph_objs import Scatter
from plotly.grid_objs import Column, Grid
from plotly.plotly.plotly import _api_v2


def random_filename():
    choice_chars = string.ascii_letters + string.digits
    random_chars = [random.choice(choice_chars) for _ in range(10)]
    unique_filename = 'Valid Grid ' + ''.join(random_chars)
    return unique_filename


def get_grid():
    c1 = Column([1, 2, 3, 4], 'first column')
    c2 = Column(['a', 'b', 'c', 'd'], 'second column')
    g = Grid([c1, c2])
    return g


def init():
    py.sign_in('PythonTest', '9v9f20pext')


def upload_and_return_grid():
    init()
    g = get_grid()
    unique_filename = random_filename()

    py.grid_ops.upload(g, unique_filename, auto_open=False)
    return g


# Nominal usage
@attr('slow')
def test_grid_upload():
    upload_and_return_grid()


@attr('slow')
@with_setup(init)
def test_grid_upload_in_new_folder():
    g = get_grid()
    path = (
        'new folder: {0}/grid in folder {1}'
        .format(random_filename(), random_filename())
    )
    py.grid_ops.upload(g, path, auto_open=False)


@attr('slow')
@with_setup(init)
def test_grid_upload_in_existing_folder():
    g = get_grid()
    folder = random_filename()
    filename = random_filename()
    py.file_ops.mkdirs(folder)
    path = (
        'existing folder: {0}/grid in folder {1}'
        .format(folder, filename)
    )
    py.grid_ops.upload(g, path, auto_open=False)


@attr('slow')
def test_column_append():
    g = upload_and_return_grid()
    new_col = Column([1, 5, 3], 'new col')

    py.grid_ops.append_columns([new_col], grid=g)


@attr('slow')
def test_row_append():
    g = upload_and_return_grid()
    new_rows = [[1, 2], [10, 20]]

    py.grid_ops.append_rows(new_rows, grid=g)


@attr('slow')
def test_plot_from_grid():
    g = upload_and_return_grid()
    url = py.plot([Scatter(xsrc=g[0], ysrc=g[1])],
                  auto_open=False, filename='plot from grid')
    return url, g


@attr('slow')
@with_setup(init)
def test_get_figure_from_references():
    url, g = test_plot_from_grid()
    fig = py.get_figure(url)
    data = fig['data']
    trace = data[0]
    assert(g[0].data == trace['x'])
    assert(g[1].data == trace['y'])

# Test grid args
_grid_id = 'chris:3043'
_grid = Grid([])
_grid.id = _grid_id
_grid_url = 'https://plot.ly/~chris/3043/my-grid'


def test_grid_id_args():
    assert(
        _api_v2.parse_grid_id_args(_grid, None) ==
        _api_v2.parse_grid_id_args(None, _grid_url)
    )


@raises(InputError)
def test_no_grid_id_args():
    _api_v2.parse_grid_id_args(None, None)


@raises(InputError)
def test_overspecified_grid_args():
    _api_v2.parse_grid_id_args(_grid, _grid_url)


# Out of order usage
@raises(InputError)
def test_scatter_from_non_uploaded_grid():
    c1 = Column([1, 2, 3, 4], 'first column')
    c2 = Column(['a', 'b', 'c', 'd'], 'second column')
    g = Grid([c1, c2])

    Scatter(xsrc=g[0], ysrc=g[1])


@attr('slow')
@raises(requests.exceptions.HTTPError)
def test_column_append_of_non_uploaded_grid():
    c1 = Column([1, 2, 3, 4], 'first column')
    c2 = Column(['a', 'b', 'c', 'd'], 'second column')
    g = Grid([c1])
    py.grid_ops.append_columns([c2], grid=g)


@attr('slow')
@raises(requests.exceptions.HTTPError)
def test_row_append_of_non_uploaded_grid():
    c1 = Column([1, 2, 3, 4], 'first column')
    rows = [[1], [2]]
    g = Grid([c1])
    py.grid_ops.append_rows(rows, grid=g)


# Input Errors
@attr('slow')
@raises(InputError)
def test_unequal_length_rows():
    g = upload_and_return_grid()
    rows = [[1, 2], ['to', 'many', 'cells']]
    py.grid_ops.append_rows(rows, grid=g)


# Test duplicate columns
@raises(InputError)
def test_duplicate_columns():
    c1 = Column([1, 2, 3, 4], 'first column')
    c2 = Column(['a', 'b', 'c', 'd'], 'first column')
    Grid([c1, c2])


# Test delete
@attr('slow')
@with_setup(init)
def test_delete_grid():
    g = get_grid()
    fn = random_filename()
    py.grid_ops.upload(g, fn, auto_open=False)
    py.grid_ops.delete(g)
    py.grid_ops.upload(g, fn, auto_open=False)


# Plotly failures
@skip('adding this for now so test_file_tools pass, more info' +
      'https://github.com/plotly/python-api/issues/262')
def test_duplicate_filenames():
    c1 = Column([1, 2, 3, 4], 'first column')
    g = Grid([c1])

    random_chars = [random.choice(string.ascii_uppercase) for _ in range(5)]
    unique_filename = 'Valid Grid ' + ''.join(random_chars)
    py.grid_ops.upload(g, unique_filename, auto_open=False)
    try:
        py.grid_ops.upload(g, unique_filename, auto_open=False)
    except PlotlyRequestError as e:
        assert(e.status_code == 409)
