"""
test_get_figure:
=================

A module intended for use with Nose.

"""


import _plotly_utils.exceptions
from chart_studio import exceptions
from chart_studio.plotly import plotly as py
from chart_studio.tests.utils import PlotlyTestCase


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
    def test_get_figure(self):
        un = "PlotlyImageTest"
        ak = "786r5mecv0"
        file_id = 13183
        py.sign_in(un, ak)
        py.get_figure("PlotlyImageTest", str(file_id))

    def test_get_figure_with_url(self):
        un = "PlotlyImageTest"
        ak = "786r5mecv0"
        url = "https://plotly.com/~PlotlyImageTest/13183/"
        py.sign_in(un, ak)
        py.get_figure(url)

    def test_get_figure_invalid_1(self):
        un = "PlotlyImageTest"
        ak = "786r5mecv0"
        url = "https://plotly.com/~PlotlyImageTest/a/"
        py.sign_in(un, ak)
        with self.assertRaises(exceptions.PlotlyError):
            py.get_figure(url)

    def test_get_figure_invalid_2(self):
        un = "PlotlyImageTest"
        ak = "786r5mecv0"
        url = "https://plotly.com/~PlotlyImageTest/-1/"
        py.sign_in(un, ak)
        with self.assertRaises(exceptions.PlotlyError):
            py.get_figure(url)

    # demonstrates error if fig has invalid parts
    def test_get_figure_invalid_3(self):
        un = "PlotlyImageTest"
        ak = "786r5mecv0"
        url = "https://plotly.com/~PlotlyImageTest/2/"
        py.sign_in(un, ak)
        with self.assertRaises(ValueError):
            py.get_figure(url)

    def test_get_figure_does_not_exist(self):
        un = "PlotlyImageTest"
        ak = "786r5mecv0"
        url = "https://plotly.com/~PlotlyImageTest/1000000000/"
        py.sign_in(un, ak)
        with self.assertRaises(_plotly_utils.exceptions.PlotlyError):
            py.get_figure(url)

    def test_get_figure_raw(self):
        un = "PlotlyImageTest"
        ak = "786r5mecv0"
        file_id = 2
        py.sign_in(un, ak)
        py.get_figure("PlotlyImageTest", str(file_id), raw=True)


class TestBytesVStrings(PlotlyTestCase):
    def test_proper_escaping(self):
        un = "PlotlyImageTest"
        ak = "786r5mecv0"
        url = "https://plotly.com/~PlotlyImageTest/13185/"
        py.sign_in(un, ak)
        py.get_figure(url)
