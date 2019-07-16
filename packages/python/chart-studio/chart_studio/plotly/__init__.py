"""
plotly
======

This module defines functionality that requires interaction between your
local machine and Plotly. Almost all functionality used here will require a
verifiable account (username/api-key pair) and a network connection.

"""
from .plotly import (
    sign_in,
    update_plot_options,
    get_credentials,
    iplot,
    plot,
    iplot_mpl,
    plot_mpl,
    get_figure,
    Stream,
    image,
    grid_ops,
    meta_ops,
    file_ops,
    get_config,
    get_grid,
    dashboard_ops,
    presentation_ops,
    create_animations,
    icreate_animations,
    parse_grid_id_args,
)
