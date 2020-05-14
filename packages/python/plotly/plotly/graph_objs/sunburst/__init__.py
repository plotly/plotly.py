import sys

if sys.version_info < (3, 7):
    from ._domain import Domain
    from ._hoverlabel import Hoverlabel
    from ._insidetextfont import Insidetextfont
    from ._leaf import Leaf
    from ._marker import Marker
    from ._outsidetextfont import Outsidetextfont
    from ._stream import Stream
    from ._textfont import Textfont
    from . import hoverlabel
    from . import marker
else:
    from _plotly_utils.importers import relative_import

    __all__, __getattr__, __dir__ = relative_import(
        __name__,
        [".hoverlabel", ".marker"],
        [
            "._domain.Domain",
            "._hoverlabel.Hoverlabel",
            "._insidetextfont.Insidetextfont",
            "._leaf.Leaf",
            "._marker.Marker",
            "._outsidetextfont.Outsidetextfont",
            "._stream.Stream",
            "._textfont.Textfont",
        ],
    )
