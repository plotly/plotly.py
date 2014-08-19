from __future__ import absolute_import

import plotly.tools as tls
import imghdr
import threading


def test_plotly_display():
    plot_info = {"un": "plotlyimagetest", "fid": "2"}
    url = "https://plot.ly/~{un}/{fid}".format(**plot_info)
    disp_obj = tls.embed(url)
    format_to_func = {
        "jpeg": jpeg_worker,
        "png": png_worker,
        "svg": svg_worker,
        "pdf": pdf_worker
    }
    results = {}
    threads = []
    for f_format, func in format_to_func.items():
        threads += [threading.Thread(target=func, args=(disp_obj, results))]
        threads[-1].setDaemon(True)
        threads[-1].start()
    for thread in threads:
        thread.join()
    for f_format in format_to_func:
        result = results.get(f_format, False)
        print("{f_format}: {result}".format(f_format=f_format, result=result))
        assert results.get(f_format)


def jpeg_worker(display_obj, results):
    img = display_obj._repr_jpeg_()
    if imghdr.what('', img) == "jpeg":
        results["jpeg"] = True


def png_worker(display_obj, results):
    img = display_obj._repr_png_()
    if imghdr.what('', img) == "png":
        results["png"] = True


def svg_worker(display_obj, results):
    img = display_obj._repr_svg_()
    if img[:4] == '<svg':
        results["svg"] = True


def pdf_worker(display_obj, results):
    img = display_obj._repr_pdf_()
    if img[:4] == '%PDF':
        results["pdf"] = True
