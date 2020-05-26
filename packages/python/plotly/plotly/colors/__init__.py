"""For a list of colors available in `plotly.colors`, please see

* the `tutorial on discrete color sequences <https://plotly.com/python/discrete-color/#color-sequences-in-plotly-express>`_
* the `list of built-in continuous color scales <https://plotly.com/python/builtin-colorscales/>`_
* the `tutorial on continuous colors <https://plotly.com/python/colorscales/>`_

Color scales and sequences are available within the following namespaces

* cyclical
* diverging
* qualitative
* sequential
"""

from __future__ import absolute_import
from _plotly_utils.colors import *  # noqa: F401

__all__ = [
    "named_colorscales",
    "cyclical",
    "diverging",
    "sequential",
    "qualitative",
]
