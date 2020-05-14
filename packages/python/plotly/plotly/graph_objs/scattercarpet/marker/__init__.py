import sys

if sys.version_info < (3, 7):
    from ._colorbar import ColorBar
    from ._gradient import Gradient
    from ._line import Line
    from . import colorbar
else:
    from _plotly_utils.importers import relative_import

    __all__, __getattr__, __dir__ = relative_import(
        __name__,
        [".colorbar"],
        ["._colorbar.ColorBar", "._gradient.Gradient", "._line.Line"],
    )
