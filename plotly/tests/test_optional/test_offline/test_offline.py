"""
test__offline

"""
from __future__ import absolute_import

from nose.tools import raises
from nose.plugins.attrib import attr
from requests.compat import json as _json

from unittest import TestCase

import plotly
from plotly import optional_imports

matplotlylib = optional_imports.get_module('plotly.matplotlylib')

if matplotlylib:
    import matplotlib
    # Force matplotlib to not use any Xwindows backend.
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt


PLOTLYJS = plotly.offline.offline.get_plotlyjs()


class PlotlyOfflineTestCase(TestCase):
    def setUp(self):
        pass

    def test_iplot_works_without_init_notebook_mode(self):
        plotly.offline.iplot([{}])

    @raises(plotly.exceptions.PlotlyError)
    def test_iplot_doesnt_work_before_you_call_init_notebook_mode_when_requesting_download(self):
        plotly.offline.iplot([{}], image='png')

    def test_iplot_works_after_you_call_init_notebook_mode(self):
        plotly.offline.init_notebook_mode()
        plotly.offline.iplot([{}])

    if matplotlylib:
        @attr('matplotlib')
        def test_iplot_mpl_works(self):
            # Generate matplotlib plot for tests
            fig = plt.figure()

            x = [10, 20, 30]
            y = [100, 200, 300]
            plt.plot(x, y)

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

    if matplotlylib:
        @attr('matplotlib')
        def test_default_mpl_plot_generates_expected_html(self):
            # Generate matplotlib plot for tests
            fig = plt.figure()

            x = [10, 20, 30]
            y = [100, 200, 300]
            plt.plot(x, y)

            figure = plotly.tools.mpl_to_plotly(fig)
            data = figure['data']
            layout = figure['layout']
            data_json = _json.dumps(data, cls=plotly.utils.PlotlyJSONEncoder)
            layout_json = _json.dumps(layout, cls=plotly.utils.PlotlyJSONEncoder)
            html = self._read_html(plotly.offline.plot_mpl(fig))

            # just make sure a few of the parts are in here
            # like PlotlyOfflineTestCase(TestCase) in test_core
            self.assertTrue(data_json.split('"uid":')[0] in html)  # data is in there
            self.assertTrue(layout_json in html)        # layout is in there too
            self.assertTrue(PLOTLYJS in html)         # and the source code
            # and it's an <html> doc
            self.assertTrue(html.startswith('<html>') and html.endswith('</html>'))
