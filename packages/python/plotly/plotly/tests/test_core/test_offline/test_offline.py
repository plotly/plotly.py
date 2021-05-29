"""
test__offline

"""
from __future__ import absolute_import

import os
from unittest import TestCase
import pytest

import json as _json

import plotly
import plotly.io as pio
from plotly.io._utils import plotly_cdn_url

import json

packages_root = os.path.dirname(
    os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(plotly.__file__))))
)

here = os.path.dirname(os.path.realpath(__file__))
html_filename = os.path.join(here, "temp-plot.html")


fig = {
    "data": [plotly.graph_objs.Scatter(x=[1, 2, 3], y=[10, 20, 30])],
    "layout": plotly.graph_objs.Layout(title="offline plot"),
}

fig_frames = {
    "data": [plotly.graph_objs.Scatter(x=[1, 2, 3], y=[10, 20, 30])],
    "layout": plotly.graph_objs.Layout(title="offline plot"),
    "frames": [{"layout": {"title": "frame 1"}}],
}

PLOTLYJS = plotly.offline.get_plotlyjs()

plotly_config_script = """\
<script type="text/javascript">\
window.PlotlyConfig = {MathJaxConfig: 'local'};</script>"""

cdn_script = '<script src="{cdn_url}"></script>'.format(cdn_url=plotly_cdn_url())

directory_script = '<script src="plotly.min.js"></script>'


mathjax_cdn = "https://cdnjs.cloudflare.com" "/ajax/libs/mathjax/2.7.5/MathJax.js"

mathjax_config_str = "?config=TeX-AMS-MML_SVG"

mathjax_cdn_script = '<script src="{cdn}{config}"></script>'.format(
    cdn=mathjax_cdn, config=mathjax_config_str
)

mathjax_font = "STIX-Web"

add_frames = "Plotly.addFrames"

do_auto_play = "Plotly.animate"

download_image = "Plotly.downloadImage"


class PlotlyOfflineBaseTestCase(TestCase):
    def tearDown(self):
        # Some offline tests produce an html file. Make sure we clean up :)
        try:
            os.remove(os.path.join(here, "temp-plot.html"))
            # Some tests that produce temp-plot.html
            # also produce plotly.min.js
            os.remove(os.path.join(here, "plotly.min.js"))
        except OSError:
            pass


class PlotlyOfflineTestCase(PlotlyOfflineBaseTestCase):
    def setUp(self):
        pio.templates.default = None

    def tearDown(self):
        pio.templates.default = "plotly"

    def _read_html(self, file_url):
        """ Read and return the HTML contents from a file_url
        in the form e.g. file:///Users/chriddyp/Repos/plotly.py/plotly-temp.html
        """
        with open(file_url.replace("file://", "").replace(" ", "")) as f:
            return f.read()

    def test_default_plot_generates_expected_html(self):
        layout_json = pio.json.to_json_plotly(fig["layout"])

        html = self._read_html(
            plotly.offline.plot(fig, auto_open=False, filename=html_filename)
        )

        # I don't really want to test the entire script output, so
        # instead just make sure a few of the parts are in here?
        self.assertIn("Plotly.newPlot", html)  # plot command is in there

        x_data = '"x":[1,2,3]'
        y_data = '"y":[10,20,30]'

        self.assertTrue(x_data in html and y_data in html)  # data in there
        self.assertIn(layout_json, html)  # so is layout
        self.assertIn(plotly_config_script, html)  # so is config
        self.assertIn(PLOTLYJS, html)  # and the source code
        # and it's an <html> doc
        self.assertTrue(html.startswith("<html>") and html.endswith("</html>"))

    def test_including_plotlyjs_truthy_html(self):
        # For backwards compatibility all truthy values that aren't otherwise
        # recognized are considered true
        for include_plotlyjs in [True, 34, "non-empty-str"]:
            html = self._read_html(
                plotly.offline.plot(
                    fig,
                    include_plotlyjs=include_plotlyjs,
                    output_type="file",
                    filename=html_filename,
                    auto_open=False,
                )
            )

            self.assertIn(plotly_config_script, html)
            self.assertIn(PLOTLYJS, html)
            self.assertNotIn(cdn_script, html)
            self.assertNotIn(directory_script, html)

    def test_including_plotlyjs_truthy_div(self):
        # For backwards compatibility all truthy values that aren't otherwise
        # recognized are considered true
        for include_plotlyjs in [True, 34, "non-empty-str"]:
            html = plotly.offline.plot(
                fig, include_plotlyjs=include_plotlyjs, output_type="div"
            )

            self.assertIn(plotly_config_script, html)
            self.assertIn(PLOTLYJS, html)
            self.assertNotIn(cdn_script, html)
            self.assertNotIn(directory_script, html)

    def test_including_plotlyjs_false_html(self):
        # For backwards compatibility all truthy values that aren't otherwise
        # recognized are considered true
        for include_plotlyjs in [False, 0, ""]:
            html = self._read_html(
                plotly.offline.plot(
                    fig,
                    include_plotlyjs=include_plotlyjs,
                    output_type="file",
                    filename=html_filename,
                    auto_open=False,
                )
            )

            self.assertNotIn(plotly_config_script, html)
            self.assertNotIn(PLOTLYJS, html)
            self.assertNotIn(cdn_script, html)
            self.assertNotIn(directory_script, html)

    def test_including_plotlyjs_false_div(self):
        for include_plotlyjs in [False, 0, ""]:
            html = plotly.offline.plot(
                fig, include_plotlyjs=include_plotlyjs, output_type="div"
            )
            self.assertNotIn(plotly_config_script, html)
            self.assertNotIn(PLOTLYJS, html)
            self.assertNotIn(cdn_script, html)
            self.assertNotIn(directory_script, html)

    def test_including_plotlyjs_cdn_html(self):
        for include_plotlyjs in ["cdn", "CDN", "Cdn"]:
            html = self._read_html(
                plotly.offline.plot(
                    fig,
                    include_plotlyjs=include_plotlyjs,
                    output_type="file",
                    filename=html_filename,
                    auto_open=False,
                )
            )
            self.assertIn(plotly_config_script, html)
            self.assertNotIn(PLOTLYJS, html)
            self.assertIn(cdn_script, html)
            self.assertNotIn(directory_script, html)

    def test_including_plotlyjs_cdn_div(self):
        for include_plotlyjs in ["cdn", "CDN", "Cdn"]:
            html = plotly.offline.plot(
                fig, include_plotlyjs=include_plotlyjs, output_type="div"
            )
            self.assertIn(plotly_config_script, html)
            self.assertNotIn(PLOTLYJS, html)
            self.assertIn(cdn_script, html)
            self.assertNotIn(directory_script, html)

    def test_including_plotlyjs_directory_html(self):
        self.assertFalse(os.path.exists(os.path.join(here, "plotly.min.js")))

        for include_plotlyjs in ["directory", "Directory", "DIRECTORY"]:
            html = self._read_html(
                plotly.offline.plot(
                    fig,
                    include_plotlyjs=include_plotlyjs,
                    filename=html_filename,
                    auto_open=False,
                )
            )
            self.assertIn(plotly_config_script, html)
            self.assertNotIn(PLOTLYJS, html)
            self.assertNotIn(cdn_script, html)
            self.assertIn(directory_script, html)

        # plot creates plotly.min.js in the output directory
        self.assertTrue(os.path.exists(os.path.join(here, "plotly.min.js")))
        with open(os.path.join(here, "plotly.min.js"), "r") as f:
            self.assertEqual(f.read(), PLOTLYJS)

    def test_including_plotlyjs_directory_div(self):
        self.assertFalse(os.path.exists(os.path.join(here, "plotly.min.js")))

        for include_plotlyjs in ["directory", "Directory", "DIRECTORY"]:
            html = plotly.offline.plot(
                fig,
                include_plotlyjs=include_plotlyjs,
                output_type="div",
                auto_open=False,
            )

            self.assertIn(plotly_config_script, html)
            self.assertNotIn(PLOTLYJS, html)
            self.assertNotIn(cdn_script, html)
            self.assertIn(directory_script, html)

        # plot does NOT create a plotly.min.js file in the output directory
        # when output_type is div
        self.assertFalse(os.path.exists("plotly.min.js"))

    def test_including_plotlyjs_path_html(self):
        for include_plotlyjs in [
            (
                "https://cdnjs.cloudflare.com/ajax/libs/plotly.js/1.40.1/"
                "plotly.min.js"
            ),
            "subpath/to/plotly.min.js",
            "something.js",
        ]:

            html = self._read_html(
                plotly.offline.plot(
                    fig,
                    include_plotlyjs=include_plotlyjs,
                    output_type="file",
                    filename=html_filename,
                    auto_open=False,
                )
            )
            self.assertNotIn(PLOTLYJS, html)
            self.assertNotIn(cdn_script, html)
            self.assertNotIn(directory_script, html)
            self.assertIn(include_plotlyjs, html)

    def test_including_plotlyjs_path_div(self):
        for include_plotlyjs in [
            (
                "https://cdnjs.cloudflare.com/ajax/libs/plotly.js/1.40.1/"
                "plotly.min.js"
            ),
            "subpath/to/plotly.min.js",
            "something.js",
        ]:

            html = plotly.offline.plot(
                fig, include_plotlyjs=include_plotlyjs, output_type="div"
            )
            self.assertNotIn(PLOTLYJS, html)
            self.assertNotIn(cdn_script, html)
            self.assertNotIn(directory_script, html)
            self.assertIn(include_plotlyjs, html)

    def test_div_output(self):
        html = plotly.offline.plot(fig, output_type="div", auto_open=False)

        self.assertNotIn("<html>", html)
        self.assertNotIn("</html>", html)
        self.assertTrue(html.startswith("<div>") and html.endswith("</div>"))

    def test_config(self):
        config = dict(linkText="Plotly rocks!", showLink=True, editable=True)
        html = self._read_html(
            plotly.offline.plot(
                fig, config=config, auto_open=False, filename=html_filename
            )
        )
        self.assertIn('"linkText": "Plotly rocks!"', html)
        self.assertIn('"showLink": true', html)
        self.assertIn('"editable": true', html)

    def test_config_bad_options(self):
        config = dict(bogus=42)

        def get_html():
            return self._read_html(
                plotly.offline.plot(
                    fig, config=config, auto_open=False, filename=html_filename
                )
            )

        # Attempts to validate warning ran into
        # https://bugs.python.org/issue29620, don't check warning for now.
        # Revisit when we move to pytest
        html = get_html()

        self.assertIn('"bogus": 42', html)

    @pytest.mark.nodev
    def test_plotlyjs_version(self):
        path = os.path.join(
            packages_root, "javascript", "jupyterlab-plotly", "package.json"
        )
        with open(path, "rt") as f:
            package_json = json.load(f)
            expected_version = package_json["dependencies"]["plotly.js"]
            if expected_version[0] == "^":
                expected_version = expected_version[1:]

        self.assertEqual(expected_version, plotly.offline.get_plotlyjs_version())

    def test_include_mathjax_false_html(self):
        html = self._read_html(
            plotly.offline.plot(
                fig,
                include_mathjax=False,
                output_type="file",
                filename=html_filename,
                auto_open=False,
            )
        )

        self.assertIn(plotly_config_script, html)
        self.assertIn(PLOTLYJS, html)
        self.assertNotIn(mathjax_cdn_script, html)
        self.assertNotIn(mathjax_font, html)

    def test_include_mathjax_false_div(self):
        html = plotly.offline.plot(fig, include_mathjax=False, output_type="div")

        self.assertIn(plotly_config_script, html)
        self.assertIn(PLOTLYJS, html)
        self.assertNotIn(mathjax_cdn_script, html)
        self.assertNotIn(mathjax_font, html)

    def test_include_mathjax_cdn_html(self):
        html = self._read_html(
            plotly.offline.plot(
                fig,
                include_mathjax="cdn",
                output_type="file",
                filename=html_filename,
                auto_open=False,
            )
        )

        self.assertIn(plotly_config_script, html)
        self.assertIn(PLOTLYJS, html)
        self.assertIn(mathjax_cdn_script, html)
        self.assertIn(mathjax_font, html)

    def test_include_mathjax_cdn_div(self):
        html = plotly.offline.plot(fig, include_mathjax="cdn", output_type="div")

        self.assertIn(plotly_config_script, html)
        self.assertIn(PLOTLYJS, html)
        self.assertIn(mathjax_cdn_script, html)
        self.assertIn(mathjax_font, html)

    def test_include_mathjax_path_html(self):
        other_cdn = "http://another/cdn/MathJax.js"
        html = self._read_html(
            plotly.offline.plot(
                fig,
                include_mathjax=other_cdn,
                output_type="file",
                filename=html_filename,
                auto_open=False,
            )
        )

        self.assertIn(plotly_config_script, html)
        self.assertIn(PLOTLYJS, html)
        self.assertNotIn(mathjax_cdn_script, html)
        self.assertIn(other_cdn + mathjax_config_str, html)
        self.assertIn(mathjax_font, html)

    def test_include_mathjax_path_div(self):
        other_cdn = "http://another/cdn/MathJax.js"
        html = plotly.offline.plot(fig, include_mathjax=other_cdn, output_type="div")

        self.assertIn(plotly_config_script, html)
        self.assertIn(PLOTLYJS, html)
        self.assertNotIn(mathjax_cdn_script, html)
        self.assertIn(other_cdn + mathjax_config_str, html)
        self.assertIn(mathjax_font, html)

    def test_auto_play(self):
        html = plotly.offline.plot(fig_frames, output_type="div")
        self.assertIn(add_frames, html)
        self.assertIn(do_auto_play, html)

    def test_no_auto_play(self):
        html = plotly.offline.plot(fig_frames, output_type="div", auto_play=False)
        self.assertIn(add_frames, html)
        self.assertNotIn(do_auto_play, html)

    def test_animation_opts(self):
        animation_opts = {"frame": {"duration": 5000}}
        expected_opts_str = json.dumps(animation_opts)

        # When auto_play is False, animation options are skipped
        html = plotly.offline.plot(
            fig_frames,
            output_type="div",
            auto_play=False,
            animation_opts=animation_opts,
        )
        self.assertIn(add_frames, html)
        self.assertNotIn(do_auto_play, html)
        self.assertNotIn(expected_opts_str, html)

        # When auto_play is True, animation options are included
        html = plotly.offline.plot(
            fig_frames, output_type="div", auto_play=True, animation_opts=animation_opts
        )
        self.assertIn(add_frames, html)
        self.assertIn(do_auto_play, html)
        self.assertIn(expected_opts_str, html)

    def test_download_image(self):
        # Not download image by default
        html = plotly.offline.plot(fig_frames, output_type="div", auto_play=False)
        self.assertNotIn(download_image, html)

        # Request download image
        html = plotly.offline.plot(
            fig_frames, output_type="div", auto_play=False, image="png"
        )
        self.assertIn(download_image, html)
