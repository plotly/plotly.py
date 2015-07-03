"""
test__offline

"""
from __future__ import absolute_import
from unittest import TestCase
import os


class PlotlyOfflineTestCase(TestCase):
    def test_initializing_before_downloading_raises_an_error(self):
        # Delete the offline directory importing plotly
        # Requires hardcoding this directory into the test
        # from utils.py because simply importing plotly will set the
        # __PLOTLY_OFFLINE_INITIALIZED flag
        PLOTLY_OFFLINE_DIRECTORY = os.path.expanduser(
            os.path.join(*'~/.plotly/plotlyjs'.split('/')))
        PLOTLY_OFFLINE_BUNDLE = os.path.join(PLOTLY_OFFLINE_DIRECTORY,
                                             'plotly-ipython-offline-bundle.js')

        try:
            os.remove(PLOTLY_OFFLINE_BUNDLE)
        except OSError:
            pass

        from plotly.exceptions import PlotlyOfflineNotFound
        import plotly

        try:
            plotly.offline.iplot([{'x': [1, 2, 3]}])
        except PlotlyOfflineNotFound:
            pass
        else:
            raise Exception("PlotlyOfflineNotFound wasn't raised")
