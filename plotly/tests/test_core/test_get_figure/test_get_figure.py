"""
test_get_figure:
=================

A module intended for use with Nose.

"""
from __future__ import absolute_import

from unittest import TestCase, skipIf

from nose.plugins.attrib import attr
from nose.tools import raises

import six

from plotly import exceptions
from plotly.graph_objs import graph_objs
from plotly.plotly import plotly as py

# username for tests: 'plotlyimagetest'
# api_key for account: '786r5mecv0'


def is_trivial(obj):
    if isinstance(obj, (dict, list)):
        if len(obj):
            if isinstance(obj, dict):
                tests = (is_trivial(obj[key]) for key in obj)
                return all(tests)
            elif isinstance(obj, list):
                tests = (is_trivial(entry) for entry in obj)
                return all(tests)
            else:
                return False
        else:
            return True
    elif obj is None:
        return True
    else:
        return False


@attr('slow')
def test_get_figure():
    un = 'PlotlyImageTest'
    ak = '786r5mecv0'
    file_id = 2
    py.sign_in(un, ak)
    print("getting: https://plot.ly/~{0}/{1}/".format(un, file_id))
    print("###########################################\n\n")
    fig = py.get_figure('PlotlyImageTest', str(file_id))


@attr('slow')
def test_get_figure_with_url():
    un = 'PlotlyImageTest'
    ak = '786r5mecv0'
    url = "https://plot.ly/~PlotlyImageTest/2/"
    py.sign_in(un, ak)
    print("getting: https://plot.ly/~PlotlyImageTest/2/")
    print("###########################################\n\n")
    fig = py.get_figure(url)


@raises(exceptions.PlotlyError)
def test_get_figure_invalid_1():
    un = 'PlotlyImageTest'
    ak = '786r5mecv0'
    url = "https://plot.ly/~PlotlyImageTest/a/"
    py.sign_in(un, ak)
    print("not getting: https://plot.ly/~PlotlyImageTest/a/")
    print("###########################################\n\n")
    fig = py.get_figure(url)


@attr('slow')
@raises(exceptions.PlotlyError)
def test_get_figure_invalid_2():
    un = 'PlotlyImageTest'
    ak = '786r5mecv0'
    url = "https://plot.ly/~PlotlyImageTest/-1/"
    py.sign_in(un, ak)
    print("not getting: https://plot.ly/~PlotlyImageTest/-1/")
    print("###########################################\n\n")
    fig = py.get_figure(url)


@attr('slow')
@raises(exceptions.PlotlyError)
def test_get_figure_does_not_exist():
    un = 'PlotlyImageTest'
    ak = '786r5mecv0'
    url = "https://plot.ly/~PlotlyImageTest/1000000000/"
    py.sign_in(un, ak)
    print("not getting: https://plot.ly/~PlotlyImageTest/1000000000/")
    print("###########################################\n\n")
    fig = py.get_figure(url)


@attr('slow')
def test_get_figure_raw():
    un = 'PlotlyImageTest'
    ak = '786r5mecv0'
    file_id = 2
    py.sign_in(un, ak)
    print("getting: https://plot.ly/~{0}/{1}/".format(un, file_id))
    print("###########################################\n\n")
    fig = py.get_figure('PlotlyImageTest', str(file_id), raw=True)


@attr('slow')
class TestBytesVStrings(TestCase):

    @skipIf(not six.PY3, 'Decoding and missing escapes only seen in PY3')
    def test_proper_escaping(self):
        un = 'PlotlyImageTest'
        ak = '786r5mecv0'
        url = "https://plot.ly/~PlotlyImageTest/91/"
        py.sign_in(un, ak)
        print("getting: https://plot.ly/~PlotlyImageTest/91/")
        print("###########################################\n\n")
        fig = py.get_figure(url)
