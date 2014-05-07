"""
matplotlylib
============

This module converts matplotlib figure objects into JSON structures which can
be understood and visualized by Plotly.

Most of the functionality should be accessed through the parent directory's
'tools' or 'plotly' modules.

"""
from . renderer import PlotlyRenderer
from . mplexporter import Exporter