"""
test_plot_mpl:
==============

A module intended for use with Nose.

"""
from __future__ import absolute_import


import _plotly_utils.exceptions
from plotly import optional_imports
from chart_studio.plotly import plotly as py
from unittest import TestCase
import pytest

matplotlylib = optional_imports.get_module("plotly.matplotlylib")

if matplotlylib:
    import matplotlib.pyplot as plt


@pytest.mark.matplotlib
class PlotMPLTest(TestCase):
    def setUp(self):
        py.sign_in("PlotlyImageTest", "786r5mecv0", plotly_domain="https://plotly.com")

    def test_update_type_error(self):
        fig, ax = plt.subplots()
        ax.plot([1, 2, 3])
        update = []
        with pytest.raises(_plotly_utils.exceptions.PlotlyGraphObjectError):
            py.plot_mpl(fig, update=update, filename="nosetests", auto_open=False)

    def test_update_validation_error(self):
        fig, ax = plt.subplots()
        ax.plot([1, 2, 3])
        update = {"invalid": "anything"}
        with pytest.raises(KeyError):
            py.plot_mpl(fig, update=update, filename="nosetests", auto_open=False)

    def test_update(self):
        fig, ax = plt.subplots()
        ax.plot([1, 2, 3])
        title = "new title"
        update = {"layout": {"title": title}}
        url = py.plot_mpl(fig, update=update, filename="nosetests", auto_open=False)
        un = url.replace("https://plotly.com/~", "").split("/")[0]
        fid = url.replace("https://plotly.com/~", "").split("/")[1]
        pfig = py.get_figure(un, fid)
        assert pfig["layout"]["title"]["text"] == title
