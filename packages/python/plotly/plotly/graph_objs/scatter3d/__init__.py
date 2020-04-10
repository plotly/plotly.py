import sys

if sys.version_info < (3, 7):
    from ._textfont import Textfont
    from ._stream import Stream
    from ._projection import Projection
    from ._marker import Marker
    from ._line import Line
    from ._hoverlabel import Hoverlabel
    from ._error_z import ErrorZ
    from ._error_y import ErrorY
    from ._error_x import ErrorX
    from . import projection
    from . import marker
    from . import line
    from . import hoverlabel
else:
    from _plotly_utils.importers import relative_import

    __all__, __getattr__ = relative_import(
        __name__,
        [".projection", ".marker", ".line", ".hoverlabel"],
        [
            "._textfont.Textfont",
            "._stream.Stream",
            "._projection.Projection",
            "._marker.Marker",
            "._line.Line",
            "._hoverlabel.Hoverlabel",
            "._error_z.ErrorZ",
            "._error_y.ErrorY",
            "._error_x.ErrorX",
        ],
    )
