"""
test__offline

"""
from __future__ import absolute_import

import os
from unittest import TestCase

from nose.plugins.attrib import attr

import plotly


class PlotlyOfflineTestCase(TestCase):

    @attr('slow')
    def test_downloading_file_saves_it_to_the_disk(self):
        dummy_js_url = ('https://gist.githubusercontent.com/chriddyp/'
                        'f40bd33d1eab6f0715dc/raw/'
                        '24cd2e4e62ceea79e6e790b3a2c94cda63510ede/test.js')

        plotly.offline.download_plotlyjs(dummy_js_url)
        assert (os.path.isfile(plotly.offline.offline.PLOTLY_OFFLINE_BUNDLE) is
                True)
