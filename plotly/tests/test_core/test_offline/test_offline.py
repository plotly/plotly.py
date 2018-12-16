"""
test__offline

"""
from __future__ import absolute_import

import os
from unittest import TestCase

from requests.compat import json as _json

import plotly
import json


fig = {
    'data': [
        plotly.graph_objs.Scatter(x=[1, 2, 3], y=[10, 20, 30])
    ],
    'layout': plotly.graph_objs.Layout(
        title='offline plot'
    )
}


resize_code_strings = [
            'window.addEventListener("resize", ',
            'Plotly.Plots.resize('
        ]


PLOTLYJS = plotly.offline.get_plotlyjs()

plotly_config_script = """\
<script type="text/javascript">\
window.PlotlyConfig = {MathJaxConfig: 'local'};</script>"""

cdn_script = ('<script src="https://cdn.plot.ly/plotly-latest.min.js">'
              '</script>')

directory_script = '<script src="plotly.min.js"></script>'


mathjax_cdn = ('https://cdnjs.cloudflare.com'
               '/ajax/libs/mathjax/2.7.5/MathJax.js')

mathjax_config_str = '?config=TeX-AMS-MML_SVG'

mathjax_cdn_script = ('<script src="{cdn}{config}"></script>'
                      .format(cdn=mathjax_cdn, config=mathjax_config_str))

mathjax_font = 'STIX-Web'


class PlotlyOfflineBaseTestCase(TestCase):
    def tearDown(self):
        # Some offline tests produce an html file. Make sure we clean up :)
        try:
            os.remove('temp-plot.html')
            # Some tests that produce temp-plot.html
            # also produce plotly.min.js
            os.remove('plotly.min.js')
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
        layout_json = _json.dumps(
            fig['layout'],
            cls=plotly.utils.PlotlyJSONEncoder)

        html = self._read_html(plotly.offline.plot(fig, auto_open=False))

        # I don't really want to test the entire script output, so
        # instead just make sure a few of the parts are in here?
        self.assertIn('Plotly.newPlot', html)  # plot command is in there

        x_data = '"x": [1, 2, 3]'
        y_data = '"y": [10, 20, 30]'

        self.assertTrue(x_data in html and y_data in html)  # data in there
        self.assertIn(layout_json, html)       # so is layout
        self.assertIn(plotly_config_script, html) # so is config
        self.assertIn(PLOTLYJS, html)          # and the source code
        # and it's an <html> doc
        self.assertTrue(html.startswith('<html>') and html.endswith('</html>'))

    def test_including_plotlyjs_truthy_html(self):
        # For backwards compatibility all truthy values that aren't otherwise
        # recognized are considered true
        for include_plotlyjs in [True, 34, 'non-empty-str']:
            html = self._read_html(plotly.offline.plot(
                fig,
                include_plotlyjs=include_plotlyjs,
                output_type='file',
                auto_open=False))

            self.assertIn(plotly_config_script, html)
            self.assertIn(PLOTLYJS, html)
            self.assertNotIn(cdn_script, html)
            self.assertNotIn(directory_script, html)

    def test_including_plotlyjs_truthy_div(self):
        # For backwards compatibility all truthy values that aren't otherwise
        # recognized are considered true
        for include_plotlyjs in [True, 34, 'non-empty-str']:
            html = plotly.offline.plot(
                fig,
                include_plotlyjs=include_plotlyjs,
                output_type='div')

            self.assertIn(plotly_config_script, html)
            self.assertIn(PLOTLYJS, html)
            self.assertNotIn(cdn_script, html)
            self.assertNotIn(directory_script, html)

    def test_including_plotlyjs_false_html(self):
        # For backwards compatibility all truthy values that aren't otherwise
        # recognized are considered true
        for include_plotlyjs in [False, 0, '']:
            html = self._read_html(plotly.offline.plot(
                fig,
                include_plotlyjs=include_plotlyjs,
                output_type='file',
                auto_open=False))

            self.assertNotIn(plotly_config_script, html)
            self.assertNotIn(PLOTLYJS, html)
            self.assertNotIn(cdn_script, html)
            self.assertNotIn(directory_script, html)

    def test_including_plotlyjs_false_div(self):
        for include_plotlyjs in [False, 0, '']:
            html = plotly.offline.plot(
                fig,
                include_plotlyjs=include_plotlyjs,
                output_type='div')
            self.assertNotIn(plotly_config_script, html)
            self.assertNotIn(PLOTLYJS, html)
            self.assertNotIn(cdn_script, html)
            self.assertNotIn(directory_script, html)

    def test_including_plotlyjs_cdn_html(self):
        for include_plotlyjs in ['cdn', 'CDN', 'Cdn']:
            html = self._read_html(plotly.offline.plot(
                fig,
                include_plotlyjs=include_plotlyjs,
                output_type='file',
                auto_open=False))
            self.assertIn(plotly_config_script, html)
            self.assertNotIn(PLOTLYJS, html)
            self.assertIn(cdn_script, html)
            self.assertNotIn(directory_script, html)

    def test_including_plotlyjs_cdn_div(self):
        for include_plotlyjs in ['cdn', 'CDN', 'Cdn']:
            html = plotly.offline.plot(
                fig,
                include_plotlyjs=include_plotlyjs,
                output_type='div')
            self.assertIn(plotly_config_script, html)
            self.assertNotIn(PLOTLYJS, html)
            self.assertIn(cdn_script, html)
            self.assertNotIn(directory_script, html)

    def test_including_plotlyjs_directory_html(self):
        self.assertFalse(os.path.exists('plotly.min.js'))

        for include_plotlyjs in ['directory', 'Directory', 'DIRECTORY']:
            html = self._read_html(plotly.offline.plot(
                fig,
                include_plotlyjs=include_plotlyjs,
                auto_open=False))
            self.assertIn(plotly_config_script, html)
            self.assertNotIn(PLOTLYJS, html)
            self.assertNotIn(cdn_script, html)
            self.assertIn(directory_script, html)

        # plot creates plotly.min.js in the output directory
        self.assertTrue(os.path.exists('plotly.min.js'))
        with open('plotly.min.js', 'r') as f:
            self.assertEqual(f.read(), PLOTLYJS)

    def test_including_plotlyjs_directory_div(self):
        self.assertFalse(os.path.exists('plotly.min.js'))

        for include_plotlyjs in ['directory', 'Directory', 'DIRECTORY']:
            html = plotly.offline.plot(
                fig,
                include_plotlyjs=include_plotlyjs,
                output_type='div',
                auto_open=False)

            self.assertIn(plotly_config_script, html)
            self.assertNotIn(PLOTLYJS, html)
            self.assertNotIn(cdn_script, html)
            self.assertIn(directory_script, html)

        # plot does NOT create a plotly.min.js file in the output directory
        # when output_type is div
        self.assertFalse(os.path.exists('plotly.min.js'))

    def test_including_plotlyjs_path_html(self):
        for include_plotlyjs in [
            ('https://cdnjs.cloudflare.com/ajax/libs/plotly.js/1.40.1/'
             'plotly.min.js'),
                'subpath/to/plotly.min.js',
                'something.js']:

            html = self._read_html(plotly.offline.plot(
                fig,
                include_plotlyjs=include_plotlyjs,
                output_type='file',
                auto_open=False))
            self.assertNotIn(PLOTLYJS, html)
            self.assertNotIn(cdn_script, html)
            self.assertNotIn(directory_script, html)
            self.assertIn(include_plotlyjs, html)

    def test_including_plotlyjs_path_div(self):
        for include_plotlyjs in [
            ('https://cdnjs.cloudflare.com/ajax/libs/plotly.js/1.40.1/'
             'plotly.min.js'),
                'subpath/to/plotly.min.js',
                'something.js']:

            html = plotly.offline.plot(
                fig,
                include_plotlyjs=include_plotlyjs,
                output_type='div')
            self.assertNotIn(PLOTLYJS, html)
            self.assertNotIn(cdn_script, html)
            self.assertNotIn(directory_script, html)
            self.assertIn(include_plotlyjs, html)

    def test_div_output(self):
        html = plotly.offline.plot(fig, output_type='div', auto_open=False)

        self.assertNotIn('<html>', html)
        self.assertNotIn('</html>', html)
        self.assertTrue(html.startswith('<div>') and html.endswith('</div>'))

    def test_autoresizing(self):

        # If width or height wasn't specified, then we add a window resizer
        html = self._read_html(plotly.offline.plot(fig, auto_open=False))
        for resize_code_string in resize_code_strings:
            self.assertIn(resize_code_string, html)

        # If width or height was specified, then we don't resize
        html = self._read_html(plotly.offline.plot({
            'data': fig['data'],
            'layout': {
                'width': 500, 'height': 500
            }
        }, auto_open=False))
        for resize_code_string in resize_code_strings:
            self.assertNotIn(resize_code_string, html)

    def test_autoresizing_div(self):

        # If width or height wasn't specified, then we add a window resizer
        for include_plotlyjs in [True, False, 'cdn', 'directory']:
            html = plotly.offline.plot(fig,
                                       output_type='div',
                                       include_plotlyjs=include_plotlyjs)

            for resize_code_string in resize_code_strings:
                self.assertIn(resize_code_string, html)

        # If width or height was specified, then we don't resize
        html = plotly.offline.plot({
            'data': fig['data'],
            'layout': {
                'width': 500, 'height': 500
            }
        }, output_type='div')

        for resize_code_string in resize_code_strings:
            self.assertNotIn(resize_code_string, html)

    def test_config(self):
        config = dict(linkText='Plotly rocks!',
                      editable=True)
        html = self._read_html(plotly.offline.plot(fig, config=config,
                                                   auto_open=False))
        self.assertIn('"linkText": "Plotly rocks!"', html)
        self.assertIn('"showLink": true', html)
        self.assertIn('"editable": true', html)

    def test_plotlyjs_version(self):
        with open('js/package.json', 'rt') as f:
            package_json = json.load(f)
            expected_version = package_json['dependencies']['plotly.js']

        self.assertEqual(expected_version,
                         plotly.offline.get_plotlyjs_version())

    def test_include_mathjax_false_html(self):
        html = self._read_html(plotly.offline.plot(
            fig,
            include_mathjax=False,
            output_type='file',
            auto_open=False))

        self.assertIn(plotly_config_script, html)
        self.assertIn(PLOTLYJS, html)
        self.assertNotIn(mathjax_cdn_script, html)
        self.assertNotIn(mathjax_font, html)

    def test_include_mathjax_false_div(self):
        html = plotly.offline.plot(
            fig,
            include_mathjax=False,
            output_type='div')

        self.assertIn(plotly_config_script, html)
        self.assertIn(PLOTLYJS, html)
        self.assertNotIn(mathjax_cdn_script, html)
        self.assertNotIn(mathjax_font, html)

    def test_include_mathjax_cdn_html(self):
        html = self._read_html(plotly.offline.plot(
            fig,
            include_mathjax='cdn',
            output_type='file',
            auto_open=False))

        self.assertIn(plotly_config_script, html)
        self.assertIn(PLOTLYJS, html)
        self.assertIn(mathjax_cdn_script, html)
        self.assertIn(mathjax_font, html)

    def test_include_mathjax_cdn_div(self):
        html = plotly.offline.plot(
            fig,
            include_mathjax='cdn',
            output_type='div')

        self.assertIn(plotly_config_script, html)
        self.assertIn(PLOTLYJS, html)
        self.assertIn(mathjax_cdn_script, html)
        self.assertIn(mathjax_font, html)

    def test_include_mathjax_path_html(self):
        other_cdn = 'http://another/cdn/MathJax.js'
        html = self._read_html(plotly.offline.plot(
            fig,
            include_mathjax=other_cdn,
            output_type='file',
            auto_open=False))

        self.assertIn(plotly_config_script, html)
        self.assertIn(PLOTLYJS, html)
        self.assertNotIn(mathjax_cdn_script, html)
        self.assertIn(other_cdn+mathjax_config_str, html)
        self.assertIn(mathjax_font, html)

    def test_include_mathjax_path_div(self):
        other_cdn = 'http://another/cdn/MathJax.js'
        html = plotly.offline.plot(
            fig,
            include_mathjax=other_cdn,
            output_type='div')

        self.assertIn(plotly_config_script, html)
        self.assertIn(PLOTLYJS, html)
        self.assertNotIn(mathjax_cdn_script, html)
        self.assertIn(other_cdn+mathjax_config_str, html)
        self.assertIn(mathjax_font, html)
