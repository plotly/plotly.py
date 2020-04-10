import sys

if sys.version_info < (3, 7):
    from ._stream import Stream
    from ._line import Line
    from ._increasing import Increasing
    from ._hoverlabel import Hoverlabel
    from ._decreasing import Decreasing
    from . import increasing
    from . import hoverlabel
    from . import decreasing
else:
    from _plotly_utils.importers import relative_import

    __all__, __getattr__ = relative_import(
        __name__,
        [".increasing", ".hoverlabel", ".decreasing"],
        [
            "._stream.Stream",
            "._line.Line",
            "._increasing.Increasing",
            "._hoverlabel.Hoverlabel",
            "._decreasing.Decreasing",
        ],
    )
