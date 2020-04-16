import sys

if sys.version_info < (3, 7):
    from ._stream import Stream
    from ._line import Line
    from ._hoverlabel import Hoverlabel
    from ._contours import Contours
    from ._colorbar import ColorBar
    from . import hoverlabel
    from . import contours
    from . import colorbar
else:
    from _plotly_utils.importers import relative_import

    __all__, __getattr__, __dir__ = relative_import(
        __name__,
        [".hoverlabel", ".contours", ".colorbar"],
        [
            "._stream.Stream",
            "._line.Line",
            "._hoverlabel.Hoverlabel",
            "._contours.Contours",
            "._colorbar.ColorBar",
        ],
    )
