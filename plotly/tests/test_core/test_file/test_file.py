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
from plotly.exceptions import PlotlyRequestError

def _random_filename():
    random_chars = [random.choice(string.ascii_uppercase) for _ in range(5)]
    unique_filename = 'Valid Folder'+''.join(random_chars)
    return unique_filename


def init():
    py.sign_in('PythonTest', '9v9f20pext')


def test_create_folder():
    init()
    py.file_ops.mkdirs(_random_filename())


def test_create_nested_folders():
    init()
    first_folder = _random_filename()
    nested_folder = '{}/{}'.format(first_folder, _random_filename())
    py.file_ops.mkdirs(nested_folder)


def test_duplicate_folders():
    init()
    first_folder = _random_filename()
    py.file_ops.mkdirs(first_folder)
    try:
        py.file_ops.mkdirs(first_folder)
    except PlotlyRequestError as e:
        if e.status_code != 409:
            raise e
