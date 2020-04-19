import sys

if sys.version_info < (3, 7):
    from ._textfont import Textfont
    from ._stream import Stream
    from ._outsidetextfont import Outsidetextfont
    from ._marker import Marker
    from ._insidetextfont import Insidetextfont
    from ._hoverlabel import Hoverlabel
    from ._connector import Connector
    from . import marker
    from . import hoverlabel
    from . import connector
else:
    from _plotly_utils.importers import relative_import

    __all__, __getattr__, __dir__ = relative_import(
        __name__,
        [".marker", ".hoverlabel", ".connector"],
        [
            "._textfont.Textfont",
            "._stream.Stream",
            "._outsidetextfont.Outsidetextfont",
            "._marker.Marker",
            "._insidetextfont.Insidetextfont",
            "._hoverlabel.Hoverlabel",
            "._connector.Connector",
        ],
    )
