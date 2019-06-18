from __future__ import absolute_import
import re as _re
import plotly.io as pio
from plotly.basedatatypes import BaseFigure
import sys

# Perform docstrings generation
def copy_doc_without_fig(from_fn, to_method):
    """
    Copy docstring from a plotly.io function to a Figure method, removing the
    fig argument docstring in the process
    """
    docstr = _re.sub(r" {4}fig:(?:.*?\n)*? {4}(\w+)", r"    \1", from_fn.__doc__)
    if sys.version_info[0] < 3:
        to_method.__func__.__doc__ = docstr
    else:
        to_method.__doc__ = docstr


copy_doc_without_fig(pio.show, BaseFigure.show)
copy_doc_without_fig(pio.to_json, BaseFigure.to_json)
copy_doc_without_fig(pio.write_json, BaseFigure.write_json)
copy_doc_without_fig(pio.to_html, BaseFigure.to_html)
copy_doc_without_fig(pio.write_html, BaseFigure.write_html)
copy_doc_without_fig(pio.to_image, BaseFigure.to_image)
copy_doc_without_fig(pio.write_image, BaseFigure.write_image)
