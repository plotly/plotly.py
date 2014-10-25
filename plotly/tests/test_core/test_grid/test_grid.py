"""
test_grid:
==========

A module intended for use with Nose.

"""

from nose.tools import raises

import random
import string
import requests

from plotly.graph_objs import Scatter
import plotly.plotly as py
import plotly.tools as tls
from plotly.grid_objs import Column, Grid
from plotly.exceptions import InputError
from nose.plugins.attrib import attr

def upload_and_return_grid():
    tls.set_config_file('https://local.plot.ly')
    py.sign_in('GridTest', 'fp4rldzhv0')

    c1 = Column('first column', [1, 2, 3, 4])
    c2 = Column('second column', ['a', 'b', 'c', 'd'])
    g = Grid([c1, c2])

    random_chars = [random.choice(string.ascii_uppercase) for _ in range(5)]
    unique_filename = 'Valid Grid '+''.join(random_chars)
    py.grid_ops.upload(g, unique_filename, auto_open=False)
    return g

## Nominal usage
def test_grid_upload():
    upload_and_return_grid()

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
        py.grid_ops._parse_grid_id_args(_grid, None, None) ==
        py.grid_ops._parse_grid_id_args(None, _grid_url, None)
    )

    assert(
        py.grid_ops._parse_grid_id_args(_grid, None, None) ==
        py.grid_ops._parse_grid_id_args(None, None, _grid_id)
    )


@raises(InputError)
def test_no_grid_id_args():
    py.grid_ops._parse_grid_id_args(None, None, None)


@raises(InputError)
def test_overspecified_grid_args():
    py.grid_ops._parse_grid_id_args(_grid, _grid_url, None)


## Out of order usage
@raises(InputError)
def test_scatter_from_non_uploaded_grid():
    c1 = Column('first column', [1, 2, 3, 4])
    c2 = Column('second column', ['a', 'b', 'c', 'd'])
    g = Grid([c1, c2])

    Scatter(xsrc=g[0], ysrc=g[1])


@raises(requests.exceptions.HTTPError)
def test_column_append_of_non_uploaded_grid():
    c1 = Column('first column', [1, 2, 3, 4])
    c2 = Column('second column', ['a', 'b', 'c', 'd'])
    g = Grid([c1])
    py.grid_ops.append_columns([c2], grid=g)


@raises(requests.exceptions.HTTPError)
def test_row_append_of_non_uploaded_grid():
    c1 = Column('first column', [1, 2, 3, 4])
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


## Plotly failures
@raises(requests.exceptions.HTTPError)
def test_duplicate_filenames():
    c1 = Column('first column', [1, 2, 3, 4])
    g = Grid([c1])

    random_chars = [random.choice(string.ascii_uppercase) for _ in range(5)]
    unique_filename = 'Valid Grid '+''.join(random_chars)
    py.grid_ops.upload(g, unique_filename, auto_open=False)
    py.grid_ops.upload(g, unique_filename, auto_open=False)
