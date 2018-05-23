"""
test_plot_mpl:
==============

A module intended for use with Nose.

"""
from __future__ import absolute_import

from nose.plugins.attrib import attr
from nose.tools import raises

from plotly import exceptions, optional_imports
from plotly.plotly import plotly as py
from unittest import TestCase

matplotlylib = optional_imports.get_module('plotly.matplotlylib')

if matplotlylib:
    import matplotlib

    # Force matplotlib to not use any Xwindows backend.
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt


@attr('matplotlib')
class PlotMPLTest(TestCase):
    def setUp(self):
        py.sign_in('PlotlyImageTest', '786r5mecv0',
                   plotly_domain='https://plot.ly')

    @raises(exceptions.PlotlyGraphObjectError)
    def test_update_type_error(self):
        fig, ax = plt.subplots()
        ax.plot([1, 2, 3])
        update = []
        py.plot_mpl(fig, update=update, filename="nosetests", auto_open=False)

    @raises(KeyError)
    def test_update_validation_error(self):
        fig, ax = plt.subplots()
        ax.plot([1, 2, 3])
        update = {'invalid': 'anything'}
        py.plot_mpl(fig, update=update, filename="nosetests", auto_open=False)

    @attr('slow')
    def test_update(self):
        fig, ax = plt.subplots()
        ax.plot([1, 2, 3])
        title = 'new title'
        update = {'layout': {'title': title}}
        url = py.plot_mpl(fig, update=update, filename="nosetests",
                          auto_open=False)
        un = url.replace("https://plot.ly/~", "").split('/')[0]
        fid = url.replace("https://plot.ly/~", "").split('/')[1]
        pfig = py.get_figure(un, fid)
        assert pfig['layout']['title'] == title
