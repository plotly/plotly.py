import sys

if sys.version_info < (3, 7):
    from ._colorbar import ColorBar
    from ._contours import Contours
    from ._line import Line
    from ._stream import Stream
    from . import colorbar
    from . import contours
else:
    from _plotly_utils.importers import relative_import

    __all__, __getattr__, __dir__ = relative_import(
        __name__,
        [".colorbar", ".contours"],
        [
            "._colorbar.ColorBar",
            "._contours.Contours",
            "._line.Line",
            "._stream.Stream",
        ],
    )
