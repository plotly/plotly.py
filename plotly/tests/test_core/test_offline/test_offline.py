"""
test__offline

"""
from __future__ import absolute_import

from unittest import TestCase

import plotly


class PlotlyOfflineTestCase(TestCase):
    def setUp(self):
        plotly.offline.offline.__PLOTLY_OFFLINE_INITIALIZED = False

    def test_iplot_doesnt_work_before_you_call_init_notebook_mode(self):
        with self.assertRaises(plotly.exceptions.PlotlyError):
            plotly.offline.iplot([{}])

    def test_iplot_works_after_you_call_init_notebook_mode(self):
        plotly.tools._ipython_imported = True
        plotly.offline.init_notebook_mode()
        plotly.offline.iplot([{}])
