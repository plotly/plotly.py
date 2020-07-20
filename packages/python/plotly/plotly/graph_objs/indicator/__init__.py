import sys

if sys.version_info < (3, 7):
    from ._delta import Delta
    from ._domain import Domain
    from ._gauge import Gauge
    from ._number import Number
    from ._stream import Stream
    from ._title import Title
    from . import delta
    from . import gauge
    from . import number
    from . import title
else:
    from _plotly_utils.importers import relative_import

    __all__, __getattr__, __dir__ = relative_import(
        __name__,
        [".delta", ".gauge", ".number", ".title"],
        [
            "._delta.Delta",
            "._domain.Domain",
            "._gauge.Gauge",
            "._number.Number",
            "._stream.Stream",
            "._title.Title",
        ],
    )
