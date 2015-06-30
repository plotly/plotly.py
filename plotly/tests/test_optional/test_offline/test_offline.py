"""
test__offline

"""
from __future__ import absolute_import
from nose.tools import raises
import os


from plotly.exceptions import PlotlyError
import plotly


@raises(PlotlyError)
def test_calling_iplot_before_initializing_raises_an_error():
    plotly.offline.iplot([{'x': [1, 2, 3]}])


def test_no_errors_are_raised_when_properly_initializing_offline_mode():
    plotly.offline.init_notebook_mode()
    plotly.offline.iplot([{'x': [1, 2, 3]}])


@raises(PlotlyError)
def test_initializing_before_downloading_raises_an_error():
    try:
        os.remove(plotly.offline.PLOTLY_OFFLINE_BUNDLE)
    except OSError:
        pass

    plotly.offline.init_notebook_mode()
