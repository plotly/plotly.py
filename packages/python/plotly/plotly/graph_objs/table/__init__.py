import sys

if sys.version_info < (3, 7):
    from ._stream import Stream
    from ._hoverlabel import Hoverlabel
    from ._header import Header
    from ._domain import Domain
    from ._cells import Cells
    from . import hoverlabel
    from . import header
    from . import cells
else:
    from _plotly_utils.importers import relative_import

    __all__, __getattr__ = relative_import(
        __name__,
        [".hoverlabel", ".header", ".cells"],
        [
            "._stream.Stream",
            "._hoverlabel.Hoverlabel",
            "._header.Header",
            "._domain.Domain",
            "._cells.Cells",
        ],
    )
