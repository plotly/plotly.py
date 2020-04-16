import sys

if sys.version_info < (3, 7):
    from ._totals import Totals
    from ._textfont import Textfont
    from ._stream import Stream
    from ._outsidetextfont import Outsidetextfont
    from ._insidetextfont import Insidetextfont
    from ._increasing import Increasing
    from ._hoverlabel import Hoverlabel
    from ._decreasing import Decreasing
    from ._connector import Connector
    from . import totals
    from . import increasing
    from . import hoverlabel
    from . import decreasing
    from . import connector
else:
    from _plotly_utils.importers import relative_import

    __all__, __getattr__, __dir__ = relative_import(
        __name__,
        [".totals", ".increasing", ".hoverlabel", ".decreasing", ".connector"],
        [
            "._totals.Totals",
            "._textfont.Textfont",
            "._stream.Stream",
            "._outsidetextfont.Outsidetextfont",
            "._insidetextfont.Insidetextfont",
            "._increasing.Increasing",
            "._hoverlabel.Hoverlabel",
            "._decreasing.Decreasing",
            "._connector.Connector",
        ],
    )
