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


def _random_filename():
    random_chars = [random.choice(string.ascii_uppercase) for _ in range(5)]
    unique_filename = 'Valid Folder'+''.join(random_chars)
    return unique_filename


def init():
    tls.set_config_file('https://local.plot.ly')
    py.sign_in('GridTest', 'fp4rldzhv0')


def test_create_folder():
    init()
    py.file_ops.mkdir(_random_filename())


def test_create_nested_folders():
    init()
    first_folder = _random_filename()
    second_folder = '{}/{}'.format(first_folder, _random_filename())
    py.file_ops.mkdir(first_folder)
    py.file_ops.mkdir(second_folder)


@raises(requests.exceptions.HTTPError) # TODO: 409, not just any 4xx
def test_duplicate_folders():
    init()
    first_folder = _random_filename()
    py.file_ops.mkdir(first_folder)
    py.file_ops.mkdir(first_folder)
