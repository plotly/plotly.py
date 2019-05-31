from __future__ import absolute_import
import re as _re
import plotly.io as pio
from plotly.basedatatypes import BaseFigure as _BaseFigure
import sys

# Perform docstrings generation
def copy_doc_without_fig(from_fn, to_method):
    """
    Copy docstring from a plotly.io function to a Figure method, removing the
    fig argument docstring in the process
    """
    docstr = _re.sub(r' {4}fig:(?:.*?\n)*? {4}(\w+)', r'    \1',
                     from_fn.__doc__)
    if sys.version_info[0] < 3:
        to_method.__func__.__doc__ = docstr
    else:
        to_method.__doc__ = docstr


copy_doc_without_fig(pio.show, _BaseFigure.show)
copy_doc_without_fig(pio.to_json, _BaseFigure.to_json)
copy_doc_without_fig(pio.write_json, _BaseFigure.write_json)
copy_doc_without_fig(pio.to_html, _BaseFigure.to_html)
copy_doc_without_fig(pio.write_html, _BaseFigure.write_html)
copy_doc_without_fig(pio.to_image, _BaseFigure.to_image)
copy_doc_without_fig(pio.write_image, _BaseFigure.write_image)

