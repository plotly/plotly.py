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


def test_downloading_file_saves_it_to_the_disk():
    dummy_js_url = ('https://gist.githubusercontent.com/chriddyp/'
                    'f40bd33d1eab6f0715dc/raw/'
                    '24cd2e4e62ceea79e6e790b3a2c94cda63510ede/test.js')

    plotly.offline.download_plotlyjs(dummy_js_url)
    assert os.path.isfile(plotly.offline.PLOTLY_OFFLINE_BUNDLE) is True


@raises(PlotlyError)
def test_initializing_before_downloading_raises_an_error():
    try:
        os.remove(plotly.offline.PLOTLY_OFFLINE_BUNDLE)
    except OSError:
        pass

    plotly.offline.init_notebook_mode()
