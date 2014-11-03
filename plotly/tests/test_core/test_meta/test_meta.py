"""
test_meta:
==========

A module intended for use with Nose.

"""

from nose.tools import raises

import random
import string
import requests

import plotly.plotly as py
import plotly.tools as tls
from plotly.grid_objs import Column, Grid
from plotly.exceptions import PlotlyRequestError


def init():
    py.sign_in('PythonTest', '9v9f20pext')


_grid = grid = Grid([Column('first column', [1, 2, 3, 4])])
_meta = {"settings":{"scope1":{"model":"Unicorn Finder","voltage":4}}}

def _random_filename():
    random_chars = [random.choice(string.ascii_uppercase) for _ in range(5)]
    unique_filename = 'Valid Grid with Meta '+''.join(random_chars)
    return unique_filename

def test_upload_meta():
    init()

    unique_filename = _random_filename()
    grid_url = py.grid_ops.upload(_grid, unique_filename, auto_open=False)

    # Add some meta data to that grid
    meta_url = py.meta_ops.upload(
        _meta,
        grid_url=grid_url)


def test_upload_meta_with_grid():
    init()

    c1 = Column('first column', [1, 2, 3, 4])
    grid = Grid([c1])

    unique_filename = _random_filename()

    py.grid_ops.upload(
        _grid,
        unique_filename,
        meta=_meta,
        auto_open=False)


@raises(PlotlyRequestError)
def test_metadata_to_nonexistent_grid():
    init()

    non_exist_meta_url = 'https://local.plot.ly/~GridTest/999999999'

    meta_url = py.meta_ops.upload(
        _meta,
        grid_url=non_exist_meta_url)
