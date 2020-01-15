"""
`plotly.express` is a terse, consistent, high-level wrapper around `plotly.graph_objects`
for rapid data exploration and figure generation. Learn more at https://plotly.express/
"""
from __future__ import absolute_import
from plotly import optional_imports
from ._imshow import imshow

pd = optional_imports.get_module("pandas")
if pd is None:
    raise ImportError(
        """\
Plotly express requires pandas to be installed."""
    )

from ._chart_types import (  # noqa: F401
    scatter,
    scatter_3d,
    scatter_polar,
    scatter_ternary,
    scatter_mapbox,
    scatter_geo,
    line,
    line_3d,
    line_polar,
    line_ternary,
    line_mapbox,
    line_geo,
    area,
    bar,
    bar_polar,
    violin,
    box,
    strip,
    histogram,
    scatter_matrix,
    parallel_coordinates,
    parallel_categories,
    choropleth,
    density_contour,
    density_heatmap,
    pie,
    sunburst,
    treemap,
    funnel,
    funnel_area,
    choropleth_mapbox,
    density_mapbox,
)


from ._core import (  # noqa: F401
    set_mapbox_access_token,
    defaults,
    get_trendline_results,
)

from . import data, colors  # noqa: F401

__all__ = [
    "scatter",
    "scatter_3d",
    "scatter_polar",
    "scatter_ternary",
    "scatter_mapbox",
    "scatter_geo",
    "scatter_matrix",
    "density_contour",
    "density_heatmap",
    "density_mapbox",
    "line",
    "line_3d",
    "line_polar",
    "line_ternary",
    "line_mapbox",
    "line_geo",
    "parallel_coordinates",
    "parallel_categories",
    "area",
    "bar",
    "bar_polar",
    "violin",
    "box",
    "strip",
    "histogram",
    "choropleth",
    "choropleth_mapbox",
    "pie",
    "sunburst",
    "treemap",
    "funnel",
    "funnel_area",
    "imshow",
    "data",
    "colors",
    "set_mapbox_access_token",
    "get_trendline_results",
]
