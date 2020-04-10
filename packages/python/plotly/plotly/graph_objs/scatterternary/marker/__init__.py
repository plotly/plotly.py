import sys

if sys.version_info < (3, 7):
    from ._line import Line
    from ._gradient import Gradient
    from ._colorbar import ColorBar
    from . import colorbar
else:
    from _plotly_utils.importers import relative_import

    __all__, __getattr__ = relative_import(
        __name__,
        [".colorbar"],
        ["._line.Line", "._gradient.Gradient", "._colorbar.ColorBar"],
    )
