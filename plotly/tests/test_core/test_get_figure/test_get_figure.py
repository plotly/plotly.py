"""
test_get_figure:
=================

A module intended for use with Nose.

"""
from __future__ import absolute_import

from unittest import TestCase, skipIf

import six
from nose.plugins.attrib import attr

from plotly import exceptions
from plotly.plotly import plotly as py
from plotly.tests.utils import PlotlyTestCase


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


class GetFigureTest(PlotlyTestCase):

    @attr('slow')
    def test_get_figure(self):
        un = 'PlotlyImageTest'
        ak = '786r5mecv0'
        file_id = 2
        py.sign_in(un, ak)
        py.get_figure('PlotlyImageTest', str(file_id))

    @attr('slow')
    def test_get_figure_with_url(self):
        un = 'PlotlyImageTest'
        ak = '786r5mecv0'
        url = "https://plot.ly/~PlotlyImageTest/2/"
        py.sign_in(un, ak)
        py.get_figure(url)

    def test_get_figure_invalid_1(self):
        un = 'PlotlyImageTest'
        ak = '786r5mecv0'
        url = "https://plot.ly/~PlotlyImageTest/a/"
        py.sign_in(un, ak)
        with self.assertRaises(exceptions.PlotlyError):
            py.get_figure(url)

    @attr('slow')
    def test_get_figure_invalid_2(self):
        un = 'PlotlyImageTest'
        ak = '786r5mecv0'
        url = "https://plot.ly/~PlotlyImageTest/-1/"
        py.sign_in(un, ak)
        with self.assertRaises(exceptions.PlotlyError):
            py.get_figure(url)

    @attr('slow')
    def test_get_figure_does_not_exist(self):
        un = 'PlotlyImageTest'
        ak = '786r5mecv0'
        url = "https://plot.ly/~PlotlyImageTest/1000000000/"
        py.sign_in(un, ak)
        with self.assertRaises(exceptions.PlotlyError):
            py.get_figure(url)

    @attr('slow')
    def test_get_figure_raw(self):
        un = 'PlotlyImageTest'
        ak = '786r5mecv0'
        file_id = 2
        py.sign_in(un, ak)
        py.get_figure('PlotlyImageTest', str(file_id), raw=True)


class TestBytesVStrings(TestCase):

    @skipIf(not six.PY3, 'Decoding and missing escapes only seen in PY3')
    def test_proper_escaping(self):
        un = 'PlotlyImageTest'
        ak = '786r5mecv0'
        url = "https://plot.ly/~PlotlyImageTest/91/"
        py.sign_in(un, ak)
        py.get_figure(url)
