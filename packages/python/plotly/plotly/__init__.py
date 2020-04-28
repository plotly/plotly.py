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
import sys
from _plotly_utils.importers import relative_import


if sys.version_info < (3, 7):
    from plotly import (
        graph_objs,
        tools,
        utils,
        offline,
        colors,
        io,
        data,
        colors,
    )
    from plotly.version import __version__

    __all__ = [
        "graph_objs",
        "tools",
        "utils",
        "offline",
        "colors",
        "io",
        "data",
        "colors",
        "__version__",
    ]

    # Set default template (for >= 3.7 this is done in ploty/io/__init__.py)
    from plotly.io import templates

    templates._default = "plotly"
else:
    __all__, __getattr__, __dir__ = relative_import(
        __name__,
        [
            ".graph_objs",
            ".graph_objects",
            ".tools",
            ".utils",
            ".offline",
            ".colors",
            ".io",
            ".data",
            ".colors",
        ],
        [".version.__version__"],
    )
