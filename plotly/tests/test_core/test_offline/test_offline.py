"""
test__offline

"""
from __future__ import absolute_import

import os
from unittest import TestCase

from requests.compat import json as _json

import plotly
from plotly.tests.utils import PlotlyTestCase


fig = {
    'data': [
        plotly.graph_objs.Scatter(x=[1, 2, 3], y=[10, 20, 30])
    ],
    'layout': plotly.graph_objs.Layout(
        title='offline plot'
    )
}

PLOTLYJS = plotly.offline.offline.get_plotlyjs()


class PlotlyOfflineBaseTestCase(TestCase):
    def tearDown(self):
        # Some offline tests produce an html file. Make sure we clean up :)
        try:
            os.remove('temp-plot.html')
        except OSError:
            pass


class PlotlyOfflineTestCase(PlotlyOfflineBaseTestCase):
    def setUp(self):
        pass

    def _read_html(self, file_url):
        """ Read and return the HTML contents from a file_url
        in the form e.g. file:///Users/chriddyp/Repos/plotly.py/plotly-temp.html
        """
        with open(file_url.replace('file://', '').replace(' ', '')) as f:
            return f.read()

    def test_default_plot_generates_expected_html(self):
        data_json = _json.dumps(fig['data'],
                                cls=plotly.utils.PlotlyJSONEncoder)
        layout_json = _json.dumps(
            fig['layout'],
            cls=plotly.utils.PlotlyJSONEncoder)

        html = self._read_html(plotly.offline.plot(fig, auto_open=False))

        # I don't really want to test the entire script output, so
        # instead just make sure a few of the parts are in here?
        self.assertTrue('Plotly.newPlot' in html) # plot command is in there
        self.assertTrue(data_json in html)        # data is in there
        self.assertTrue(layout_json in html)      # so is layout
        self.assertTrue(PLOTLYJS in html)         # and the source code
        # and it's an <html> doc
        self.assertTrue(html.startswith('<html>') and html.endswith('</html>'))

    def test_including_plotlyjs(self):
        html = self._read_html(plotly.offline.plot(fig, include_plotlyjs=False,
                                                   auto_open=False))
        self.assertTrue(PLOTLYJS not in html)

    def test_div_output(self):
        html = plotly.offline.plot(fig, output_type='div', auto_open=False)

        self.assertTrue('<html>' not in html and '</html>' not in html)
        self.assertTrue(html.startswith('<div>') and html.endswith('</div>'))

    def test_autoresizing(self):
        resize_code_strings = [
            'window.addEventListener("resize", ',
            'Plotly.Plots.resize('
        ]
        # If width or height wasn't specified, then we add a window resizer
        html = self._read_html(plotly.offline.plot(fig, auto_open=False))
        for resize_code_string in resize_code_strings:
            self.assertTrue(resize_code_string in html)

        # If width or height was specified, then we don't resize
        html = plotly.offline.plot({
            'data': fig['data'],
            'layout': {
                'width': 500, 'height': 500
            }
        }, auto_open=False)
        for resize_code_string in resize_code_strings:
            self.assertTrue(resize_code_string not in html)


class PlotlyOfflineOtherDomainTestCase(PlotlyOfflineBaseTestCase):
    def setUp(self):
        super(PlotlyOfflineOtherDomainTestCase, self).setUp()
        plotly.tools.set_config_file(plotly_domain='https://stage.plot.ly',
                                     plotly_api_domain='https://api-stage.plot.ly')
        plotly.plotly.sign_in('PlotlyTestShark', 'kI2H0E7sTZ5RM9yoaK4X')

    def test_plot_rendered_if_non_plotly_domain(self):
        html = plotly.offline.plot(fig, output_type='div')

        # test that 'Export to stage.plot.ly' is in the html
        self.assertTrue('Export to stage.plot.ly' in html)

    def tearDown(self):
        plotly.tools.set_config_file(plotly_domain='https://plot.ly',
                                     plotly_api_domain='https://api.plot.ly')
        plotly.plotly.sign_in('PythonTest', '9v9f20pext')
        super(PlotlyOfflineOtherDomainTestCase, self).tearDown()
