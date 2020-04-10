import sys

if sys.version_info < (3, 7):
    from ._tickfont import Tickfont
    from ._stream import Stream
    from ._line import Line
    from ._labelfont import Labelfont
    from ._domain import Domain
    from ._dimension import Dimension
    from . import line
else:
    from _plotly_utils.importers import relative_import

    __all__, __getattr__ = relative_import(
        __name__,
        [".line"],
        [
            "._tickfont.Tickfont",
            "._stream.Stream",
            "._line.Line",
            "._labelfont.Labelfont",
            "._domain.Domain",
            "._dimension.Dimension",
        ],
    )
