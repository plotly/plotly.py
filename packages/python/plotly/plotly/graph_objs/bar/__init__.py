import sys

if sys.version_info < (3, 7):
    from ._unselected import Unselected
    from ._textfont import Textfont
    from ._stream import Stream
    from ._selected import Selected
    from ._outsidetextfont import Outsidetextfont
    from ._marker import Marker
    from ._insidetextfont import Insidetextfont
    from ._hoverlabel import Hoverlabel
    from ._error_y import ErrorY
    from ._error_x import ErrorX
    from . import unselected
    from . import selected
    from . import marker
    from . import hoverlabel
else:
    from _plotly_utils.importers import relative_import

    __all__, __getattr__ = relative_import(
        __name__,
        [".unselected", ".selected", ".marker", ".hoverlabel"],
        [
            "._unselected.Unselected",
            "._textfont.Textfont",
            "._stream.Stream",
            "._selected.Selected",
            "._outsidetextfont.Outsidetextfont",
            "._marker.Marker",
            "._insidetextfont.Insidetextfont",
            "._hoverlabel.Hoverlabel",
            "._error_y.ErrorY",
            "._error_x.ErrorX",
        ],
    )
