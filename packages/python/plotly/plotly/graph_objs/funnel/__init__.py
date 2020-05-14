import sys

if sys.version_info < (3, 7):
    from ._connector import Connector
    from ._hoverlabel import Hoverlabel
    from ._insidetextfont import Insidetextfont
    from ._marker import Marker
    from ._outsidetextfont import Outsidetextfont
    from ._stream import Stream
    from ._textfont import Textfont
    from . import connector
    from . import hoverlabel
    from . import marker
else:
    from _plotly_utils.importers import relative_import

    __all__, __getattr__, __dir__ = relative_import(
        __name__,
        [".connector", ".hoverlabel", ".marker"],
        [
            "._connector.Connector",
            "._hoverlabel.Hoverlabel",
            "._insidetextfont.Insidetextfont",
            "._marker.Marker",
            "._outsidetextfont.Outsidetextfont",
            "._stream.Stream",
            "._textfont.Textfont",
        ],
    )
