import sys

if sys.version_info < (3, 7):
    from ._tiling import Tiling
    from ._textfont import Textfont
    from ._stream import Stream
    from ._pathbar import Pathbar
    from ._outsidetextfont import Outsidetextfont
    from ._marker import Marker
    from ._insidetextfont import Insidetextfont
    from ._hoverlabel import Hoverlabel
    from ._domain import Domain
    from . import pathbar
    from . import marker
    from . import hoverlabel
else:
    from _plotly_utils.importers import relative_import

    __all__, __getattr__ = relative_import(
        __name__,
        [".pathbar", ".marker", ".hoverlabel"],
        [
            "._tiling.Tiling",
            "._textfont.Textfont",
            "._stream.Stream",
            "._pathbar.Pathbar",
            "._outsidetextfont.Outsidetextfont",
            "._marker.Marker",
            "._insidetextfont.Insidetextfont",
            "._hoverlabel.Hoverlabel",
            "._domain.Domain",
        ],
    )
