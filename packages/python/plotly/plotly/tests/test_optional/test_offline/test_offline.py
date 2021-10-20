"""
test__offline

"""
from __future__ import absolute_import
import re
import json as _json

from unittest import TestCase
import pytest

import plotly
import plotly.io as pio
from plotly import optional_imports

matplotlylib = optional_imports.get_module("plotly.matplotlylib")

if matplotlylib:
    import matplotlib

    # Force matplotlib to not use any Xwindows backend.
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt


PLOTLYJS = plotly.offline.offline.get_plotlyjs()


class PlotlyOfflineTestCase(TestCase):
    def setUp(self):
        pass

    def test_iplot_works_without_init_notebook_mode(self):
        plotly.offline.iplot([{}])

    def test_iplot_works_after_you_call_init_notebook_mode(self):
        plotly.offline.init_notebook_mode()
        plotly.offline.iplot([{}])

    if matplotlylib:

        @pytest.mark.matplotlib
        def test_iplot_mpl_works(self):
            plotly.offline.init_notebook_mode()
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
        with open(file_url.replace("file://", "").replace(" ", "")) as f:
            return f.read()

    if matplotlylib:

        @pytest.mark.matplotlib
        def test_default_mpl_plot_generates_expected_html(self):
            # Generate matplotlib plot for tests
            fig = plt.figure()

            x = [10, 20, 30]
            y = [100, 200, 300]
            plt.plot(x, y)

            figure = plotly.tools.mpl_to_plotly(fig).to_dict()
            data = figure["data"]

            layout = figure["layout"]
            data_json = pio.json.to_json_plotly(data)
            layout_json = pio.json.to_json_plotly(layout)
            html = self._read_html(plotly.offline.plot_mpl(fig))

            # blank out uid before comparisons
            data_json = re.sub('"uid": "[^"]+"', '"uid": ""', data_json)
            html = re.sub('"uid": "[^"]+"', '"uid": ""', html)

            # just make sure a few of the parts are in here
            # like PlotlyOfflineTestCase(TestCase) in test_core
            self.assertTrue(data_json in html)  # data is in there
            self.assertTrue(PLOTLYJS in html)  # and the source code
            # and it's an <html> doc
            self.assertTrue(html.startswith("<html>") and html.endswith("</html>"))
