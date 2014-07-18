"""
test_plot_mpl:
==============

A module intended for use with Nose.

"""
from __future__ import absolute_import

from plotly.plotly import plotly as py
from plotly import exceptions
from nose.tools import raises
import matplotlib
# Force matplotlib to not use any Xwindows backend.
matplotlib.use('Agg')
import matplotlib.pyplot as plt

py.sign_in('test-runner', '9h29fe3l0x')

@raises(exceptions.PlotlyError)
def test_update_type_error():
    fig, ax = plt.subplots()
    ax.plot([1, 2, 3])
    update = []
    py.plot_mpl(fig, update=update, filename="nosetests", auto_open=False)


@raises(exceptions.PlotlyError)
def test_update_validation_error():
    fig, ax = plt.subplots()
    ax.plot([1, 2, 3])
    update = {'invalid': 'anything'}
    py.plot_mpl(fig, update=update, filename="nosetests", auto_open=False)


def test_update():
    fig, ax = plt.subplots()
    ax.plot([1, 2, 3])
    title = 'new title'
    update = {'layout': {'title': title}}
    url = py.plot_mpl(fig, update=update, filename="nosetests", auto_open=False)
    un = url.replace("https://plot.ly/~", "").split('/')[0]
    fid = url.replace("https://plot.ly/~", "").split('/')[1]
    pfig = py.get_figure(un, fid)
    assert pfig['layout']['title'] == title