"""
https://plot.ly/python/

Plotly's Python API allows users to programmatically access Plotly's
server resources.

This package is organized as follows:

Subpackages:

- plotly: all functionality that requires access to Plotly's servers

- graph_objs: objects for designing figures and visualizing data

- matplotlylib: tools to convert matplotlib figures

Modules:

- tools: some helpful tools that do not require access to Plotly's servers

- utils: functions that you probably won't need, but that subpackages use

- version: holds the current API version

- exceptions: defines our custom exception classes

"""
from __future__ import absolute_import

# https://packaging.python.org/guides/packaging-namespace-packages/
#         pkgutil-style-namespace-packages
__path__ = __import__('pkgutil').extend_path(__path__, __name__)

from plotly import (
    graph_objs,
    tools,
    utils,
    offline,
    colors,
    io,
    _docstring_gen
)

from plotly.version import __version__

# Set default template here to make sure import process is complete
io.templates._default = 'plotly'
