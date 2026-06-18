# ruff: noqa: E402

from plotly import optional_imports

# Require that numpy exists for figure_factory
np = optional_imports.get_module("numpy")
if np is None:
    raise ImportError(
        """\
The figure factory module requires the numpy package"""
    )


from plotly.figure_factory._dendrogram import create_dendrogram
from plotly.figure_factory._quiver import create_quiver
from plotly.figure_factory._streamline import create_streamline
from plotly.figure_factory._table import create_table
from plotly.figure_factory._trisurf import create_trisurf

if optional_imports.get_module("pandas") is not None:
    from plotly.figure_factory._hexbin_map import create_hexbin_map
else:

    def create_hexbin_map(*args, **kwargs):
        raise ImportError("Please install pandas to use `create_hexbin_map`")


if optional_imports.get_module("skimage") is not None:
    from plotly.figure_factory._ternary_contour import create_ternary_contour
else:

    def create_ternary_contour(*args, **kwargs):
        raise ImportError("Please install scikit-image to use `create_ternary_contour`")


__all__ = [
    "create_dendrogram",
    "create_hexbin_map",
    "create_quiver",
    "create_streamline",
    "create_table",
    "create_ternary_contour",
    "create_trisurf",
]
