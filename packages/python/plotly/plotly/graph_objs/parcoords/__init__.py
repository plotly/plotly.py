import sys

if sys.version_info < (3, 7):
    from ._dimension import Dimension
    from ._domain import Domain
    from ._labelfont import Labelfont
    from ._line import Line
    from ._rangefont import Rangefont
    from ._stream import Stream
    from ._tickfont import Tickfont
    from . import line
else:
    from _plotly_utils.importers import relative_import

    __all__, __getattr__, __dir__ = relative_import(
        __name__,
        [".line"],
        [
            "._dimension.Dimension",
            "._domain.Domain",
            "._labelfont.Labelfont",
            "._line.Line",
            "._rangefont.Rangefont",
            "._stream.Stream",
            "._tickfont.Tickfont",
        ],
    )
