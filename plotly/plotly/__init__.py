"""
plotly
======

This module defines functionality that requires interaction between your
local machine and Plotly. Almost all functionality used here will required a
verifiable account and an internet connection.

Classes:
    image
    Stream

Functions:
    sign_in
    iplot
    plot
    iplot_mpl
    plot_mpl
    get_figure
    update_plot_options
    get_plot_options
    get_credentials

"""
from plotly import *

__all__ = ["sign_in", "update_plot_options", "get_plot_options",
           "get_credentials", "iplot", "plot", "iplot_mpl", "plot_mpl",
           "get_figure", "Stream", "image"]
