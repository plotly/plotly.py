from __future__ import absolute_import
import re as _re
import plotly.io as pio
from plotly.basedatatypes import BaseFigure as _BaseFigure


# Perform docstrings generation
def _remove_fig_docstr(docstr):
    """
    Remove the fig argument from the input docstring and return the result
    """
    return _re.sub(r' {4}fig:(?:.*?\n)*? {4}(\w+)', r'    \1', docstr)


_BaseFigure.show.__doc__ = _remove_fig_docstr(pio.show.__doc__)
_BaseFigure.to_json.__doc__ = _remove_fig_docstr(pio.to_json.__doc__)
_BaseFigure.write_json.__doc__ = _remove_fig_docstr(pio.write_json.__doc__)
_BaseFigure.to_html.__doc__ = _remove_fig_docstr(pio.to_html.__doc__)
_BaseFigure.write_html.__doc__ = _remove_fig_docstr(pio.write_html.__doc__)
_BaseFigure.to_image.__doc__ = _remove_fig_docstr(pio.to_image.__doc__)
_BaseFigure.write_image.__doc__ = _remove_fig_docstr(pio.write_image.__doc__)
