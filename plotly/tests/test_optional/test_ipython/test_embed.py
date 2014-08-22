from __future__ import absolute_import

import plotly.tools as tls
import imghdr
import threading
import unittest


class TestPlotlyDisplay(unittest.TestCase):

    def setUp(self):
        plot_info = {"un": "plotlyimagetest", "fid": "2"}
        url = "https://plot.ly/~{un}/{fid}".format(**plot_info)
        self.display_obj = tls.embed(url)
        self.results = {}
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
            assert self.results.get(f_format)

    def jpeg_worker(self):
        img = self.display_obj._repr_jpeg_()
        if imghdr.what('', img) == "jpeg":
            self.results["jpeg"] = True

    def png_worker(self):
        img = self.display_obj._repr_png_()
        if imghdr.what('', img) == "png":
            self.results["png"] = True

    def svg_worker(self):
        img = self.display_obj._repr_svg_()
        if img[:4] == '<svg':
            self.results["svg"] = True

    def pdf_worker(self):
        img = self.display_obj._repr_pdf_()
        if img[:4] == '%PDF':
            self.results["pdf"] = True
