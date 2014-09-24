from __future__ import absolute_import

import plotly.tools as tls
import imghdr
import threading
import six
import unittest
version = six.sys.version_info[:2]  # need this for conditional testing

# unittest `skipIf` not supported in 2.6 and IPython not supported in 2.6/3.2
if version < (2, 7) or (2, 7) < version < (3, 3):
    pass
else:

    class TestPlotlyDisplay(unittest.TestCase):

        def setUp(self):
            plot_info = {"un": "PlotlyImageTest", "fid": "2"}
            url = "https://plot.ly/~{un}/{fid}".format(**plot_info)
            self.display_obj = tls.embed(url)
            self.results = {}
            self.images = {}
            self.threads = []
            self.format_to_func = {
                "jpeg": self.jpeg_worker,
                "png": self.png_worker,
                "svg": self.svg_worker,
                "pdf": self.pdf_worker}

        def test_plotly_display(self):
            for f_format, func in self.format_to_func.items():
                self.threads += [threading.Thread(target=func)]
                self.threads[-1].setDaemon(True)
                self.threads[-1].start()
            for thread in self.threads:
                thread.join()
            for f_format in self.format_to_func:
                result = self.results.get(f_format, False)
                print("{f_format}: {result}".format(f_format=f_format,
                                                    result=result))
                print("{image}\n".format(image=self.images[f_format][:72]))
                assert self.results.get(f_format)

        def jpeg_worker(self):
            self.images['jpeg'] = self.display_obj._repr_jpeg_()
            if imghdr.what('', self.images['jpeg']) == "jpeg":
                self.results["jpeg"] = True

        def png_worker(self):
            self.images['png'] = self.display_obj._repr_png_()
            if imghdr.what('', self.images['png']) == "png":
                self.results["png"] = True

        def svg_worker(self):
            self.images['svg'] = self.display_obj._repr_svg_()
            if self.images['svg'][:4] == six.b('<svg'):
                self.results["svg"] = True

        def pdf_worker(self):
            self.images['pdf'] = self.display_obj._repr_pdf_()
            if self.images['pdf'][:4] == six.b('%PDF'):
                self.results["pdf"] = True
