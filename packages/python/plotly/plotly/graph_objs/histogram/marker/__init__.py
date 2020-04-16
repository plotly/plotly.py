import sys

if sys.version_info < (3, 7):
    from ._line import Line
    from ._colorbar import ColorBar
    from . import colorbar
else:
    from _plotly_utils.importers import relative_import

    __all__, __getattr__, __dir__ = relative_import(
        __name__, [".colorbar"], ["._line.Line", "._colorbar.ColorBar"]
    )
