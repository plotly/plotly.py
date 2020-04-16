import sys

if sys.version_info < (3, 7):
    from ._title import Title
    from ._stream import Stream
    from ._number import Number
    from ._gauge import Gauge
    from ._domain import Domain
    from ._delta import Delta
    from . import title
    from . import number
    from . import gauge
    from . import delta
else:
    from _plotly_utils.importers import relative_import

    __all__, __getattr__, __dir__ = relative_import(
        __name__,
        [".title", ".number", ".gauge", ".delta"],
        [
            "._title.Title",
            "._stream.Stream",
            "._number.Number",
            "._gauge.Gauge",
            "._domain.Domain",
            "._delta.Delta",
        ],
    )
