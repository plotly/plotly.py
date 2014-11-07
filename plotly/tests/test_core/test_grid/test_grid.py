"""
test_grid:
==========

A module intended for use with Nose.

"""

from nose.tools import raises

import random
import string
from nose.plugins.attrib import attr

from plotly.graph_objs import Scatter
import plotly.plotly as py
import plotly.tools as tls
from plotly.grid_objs import Column, Grid
from plotly.exceptions import InputError, PlotlyRequestError


def _random_filename():
    random_chars = [random.choice(string.ascii_uppercase) for _ in range(5)]
    unique_filename = 'Valid Grid '+''.join(random_chars)
    return unique_filename


def _get_grid():
    c1 = Column('first column', [1, 2, 3, 4])
    c2 = Column('second column', ['a', 'b', 'c', 'd'])
    g = Grid([c1, c2])
    return g


def _init():
    py.sign_in('PythonTest', '9v9f20pext')


def upload_and_return_grid():
    _init()
    g = _get_grid()
    unique_filename = _random_filename()

    py.grid_ops.upload(g, unique_filename, auto_open=False)
    return g


## Nominal usage
def test_grid_upload():
    upload_and_return_grid()


def test_grid_upload_in_new_folder():
    _init()
    g = _get_grid()
    path = 'new folder: {}/grid in folder {}'.format(_random_filename(), _random_filename())
    py.grid_ops.upload(g, path, auto_open=False)


def test_grid_upload_in_existing_folder():
    _init()
    g = _get_grid()
    folder = _random_filename()
    filename = _random_filename()
    py.file_ops.mkdirs(folder)
    path = 'existing folder: {}/grid in folder {}'.format(folder, filename)
    py.grid_ops.upload(g, path, auto_open=False)


def test_column_append():
    g = upload_and_return_grid()
    new_col = Column('new col', [1, 5, 3])

    py.grid_ops.append_columns([new_col], grid=g)


def test_row_append():
    g = upload_and_return_grid()
    new_rows = [[1, 2], [10, 20]]

    py.grid_ops.append_rows(new_rows, grid=g)


def test_plot_from_grid():
    g = upload_and_return_grid()
    url = py.plot([Scatter(xsrc=g[0], ysrc=g[1])],
                  auto_open=False, filename='plot from grid')
    return url, g


def test_get_figure_from_references():
    url, g = test_plot_from_grid()
    fig = py.get_figure(url)
    data = fig['data']
    trace = data[0]
    assert(g[0].data == trace['x'])
    assert(g[1].data == trace['y'])

## Test grid args
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


## Out of order usage
@raises(InputError)
def test_scatter_from_non_uploaded_grid():
    c1 = Column([1, 2, 3, 4], 'first column')
    c2 = Column(['a', 'b', 'c', 'd'], 'second column')
    g = Grid([c1, c2])

    Scatter(xsrc=g[0], ysrc=g[1])


@raises(PlotlyRequestError)
def test_column_append_of_non_uploaded_grid():
    c1 = Column([1, 2, 3, 4], 'first column')
    c2 = Column(['a', 'b', 'c', 'd'], 'second column')
    g = Grid([c1])
    py.grid_ops.append_columns([c2], grid=g)


@raises(PlotlyRequestError)
def test_row_append_of_non_uploaded_grid():
    c1 = Column([1, 2, 3, 4], 'first column')
    rows = [[1], [2]]
    g = Grid([c1])
    py.grid_ops.append_rows(rows, grid=g)


## Input Errors
@raises(InputError)
def test_unequal_length_rows():
    g = upload_and_return_grid()
    rows = [[1, 2], ['to', 'many', 'cells']]
    py.grid_ops.append_rows(rows, grid=g)


# Test duplicate columns
@raises(InputError)
def test_duplicate_columns():
    c1 = Column('first column', [1, 2, 3, 4])
    c2 = Column('first column', ['a', 'b', 'c', 'd'])
    Grid([c1, c2])


# Test delete
def test_delete_grid():
    _init()
    g = _get_grid()
    fn = _random_filename()
    py.grid_ops.upload(g, fn, auto_open=False)
    py.grid_ops.delete(g)
    py.grid_ops.upload(g, fn, auto_open=False)


## Plotly failures
def test_duplicate_filenames():
    c1 = Column('first column', [1, 2, 3, 4])
    g = Grid([c1])

    random_chars = [random.choice(string.ascii_uppercase) for _ in range(5)]
    unique_filename = 'Valid Grid '+''.join(random_chars)
    py.grid_ops.upload(g, unique_filename, auto_open=False)
    try:
        py.grid_ops.upload(g, unique_filename, auto_open=False)
    except PlotlyRequestError as e:
        if e.status_code != 409:
            raise e

