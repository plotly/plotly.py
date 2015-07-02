"""
test__offline

"""
from __future__ import absolute_import
from nose.tools import raises
from unittest import TestCase
import os

from plotly.exceptions import PlotlyOfflineNotFound
import plotly


class PlotlyOfflineTestCase(TestCase):
    @raises(PlotlyOfflineNotFound)
    def test_initializing_before_downloading_raises_an_error(self):
        try:
            os.remove(plotly.offline.offline.PLOTLY_OFFLINE_BUNDLE)
        except OSError:
            pass

        plotly.offline.iplot([{'x': [1, 2, 3]}])
