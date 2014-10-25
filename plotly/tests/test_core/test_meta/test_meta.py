"""
test_grid:
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
from nose.plugins.attrib import attr


def test_upload_meta():
    tls.set_config_file('https://local.plot.ly')
    py.sign_in('GridTest', 'fp4rldzhv0')

    # First, create a grid
    c1 = Column('first column', [1, 2, 3, 4])
    grid = Grid([c1])
    random_chars = [random.choice(string.ascii_uppercase) for _ in range(5)]
    unique_filename = 'Valid Grid with Meta '+''.join(random_chars)
    grid_url = py.grid_ops.upload(grid, unique_filename, auto_open=False)

    # Add some meta data to that grid
    meta = {"settings": {"scope1": {"model": "Unicorn Finder", "voltage": 4}}}
    meta_url = py.meta_ops.upload(
        meta,
        grid_url=grid_url)


def test_upload_meta_with_grid():
    tls.set_config_file('https://local.plot.ly')
    py.sign_in('GridTest', 'fp4rldzhv0')

    c1 = Column('first column', [1, 2, 3, 4])
    grid = Grid([c1])
    meta = {"settings":{"scope1":{"model":"Unicorn Finder","voltage":4}}}
    random_chars = [random.choice(string.ascii_uppercase) for _ in range(5)]
    unique_filename = 'Valid Grid '+''.join(random_chars)
    py.grid_ops.upload(
        grid,
        unique_filename,
        meta=meta,
        auto_open=False)
