import sys

if sys.version_info < (3, 7):
    from ._title import Title
    from ._textfont import Textfont
    from ._stream import Stream
    from ._marker import Marker
    from ._insidetextfont import Insidetextfont
    from ._hoverlabel import Hoverlabel
    from ._domain import Domain
    from . import title
    from . import marker
    from . import hoverlabel
else:
    from _plotly_utils.importers import relative_import

    __all__, __getattr__ = relative_import(
        __name__,
        [".title", ".marker", ".hoverlabel"],
        [
            "._title.Title",
            "._textfont.Textfont",
            "._stream.Stream",
            "._marker.Marker",
            "._insidetextfont.Insidetextfont",
            "._hoverlabel.Hoverlabel",
            "._domain.Domain",
        ],
    )
