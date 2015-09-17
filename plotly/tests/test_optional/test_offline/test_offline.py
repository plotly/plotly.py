"""
test__offline

"""
from __future__ import absolute_import

import os
from nose.plugins.attrib import attr
from nose.tools import raises
from unittest import TestCase

import plotly
from plotly.exceptions import PlotlyError

dummy_js_url = ('https://gist.githubusercontent.com/chriddyp/'
                'f40bd33d1eab6f0715dc/raw/'
                '24cd2e4e62ceea79e6e790b3a2c94cda63510ede/'
                'test.js')


class PlotlyOfflineTestCase(TestCase):
    def _remove_plotlyjs(self):
        try:
            os.remove(plotly.offline.offline.PLOTLY_OFFLINE_BUNDLE)
        except OSError:
            pass

    def test_no_errors_are_raised_when_initializing_offline_mode(self):
        self._remove_plotlyjs()
        plotly.offline.download_plotlyjs(dummy_js_url)
        plotly.offline.init_notebook_mode()
        plotly.offline.iplot([{'x': [1, 2, 3]}])

    @attr('slow')
    @raises(PlotlyError)
    def test_calling_iplot_before_initializing_raises_an_error(self):
        self._remove_plotlyjs()
        plotly.offline.download_plotlyjs(dummy_js_url)
        plotly.offline.iplot([{'x': [1, 2, 3]}])

    @raises(PlotlyError)
    def test_initializing_before_downloading_raises_an_error(self):
        self._remove_plotlyjs()
        plotly.offline.init_notebook_mode()
