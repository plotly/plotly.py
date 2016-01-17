"""
test__offline

"""
from __future__ import absolute_import

from nose.tools import raises
from nose.plugins.attrib import attr

from unittest import TestCase
import json

import plotly

# TODO: matplotlib-build-wip
from plotly.tools import _matplotlylib_imported

if _matplotlylib_imported:
    import matplotlib
    # Force matplotlib to not use any Xwindows backend.
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt


PLOTLYJS = plotly.offline.offline.get_plotlyjs()


class PlotlyOfflineTestCase(TestCase):
    def setUp(self):
        plotly.offline.offline.__PLOTLY_OFFLINE_INITIALIZED = False

    @raises(plotly.exceptions.PlotlyError)
    def test_iplot_doesnt_work_before_you_call_init_notebook_mode(self):
        plotly.offline.iplot([{}])

    def test_iplot_works_after_you_call_init_notebook_mode(self):
        plotly.tools._ipython_imported = True
        plotly.offline.init_notebook_mode()
        plotly.offline.iplot([{}])

    @attr('matplotlib')
    def test_iplot_mpl_works_after_you_call_init_notebook_mode(self):
        # Generate matplotlib plot for tests
        fig = plt.figure()

        x = [10, 20, 30]
        y = [100, 200, 300]
        plt.plot(x, y, "o")

        plotly.tools._ipython_imported = True
        plotly.offline.init_notebook_mode()
        plotly.offline.iplot_mpl(fig)


class PlotlyOfflineMPLTestCase(TestCase):
    def setUp(self):
        pass

    def _read_html(self, file_url):
        """ Read and return the HTML contents from a file_url in the
        form e.g. file:///Users/chriddyp/Repos/plotly.py/plotly-temp.html
        """
        with open(file_url.replace('file://', '').replace(' ', '')) as f:
            return f.read()

    @attr('matplotlib')
    def test_default_mpl_plot_generates_expected_html(self):
        # Generate matplotlib plot for tests
        fig = plt.figure()

        x = [10, 20, 30]
        y = [100, 200, 300]
        plt.plot(x, y, "o")

        figure = plotly.tools.mpl_to_plotly(fig)
        data = figure['data']
        layout = figure['layout']
        data_json = json.dumps(data, cls=plotly.utils.PlotlyJSONEncoder)
        layout_json = json.dumps(layout, cls=plotly.utils.PlotlyJSONEncoder)
        html = self._read_html(plotly.offline.plot_mpl(fig))

        # just make sure a few of the parts are in here
        # like PlotlyOfflineTestCase(TestCase) in test_core
        self.assertTrue('Plotly.newPlot' in html) # plot command is in there
        self.assertTrue(data_json in html)        # data is in there
        self.assertTrue(layout_json in html)        # layout is in there too
        self.assertTrue(PLOTLYJS in html)         # and the source code
        # and it's an <html> doc
        self.assertTrue(html.startswith('<html>') and html.endswith('</html>'))

