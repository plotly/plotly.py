import sys
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ._pattern import PatternValidator
    from ._line import LineValidator
    from ._colorssrc import ColorssrcValidator
    from ._colors import ColorsValidator
else:
    from _plotly_utils.importers import relative_import

    __all__, __getattr__, __dir__ = relative_import(
        __name__,
        [],
        [
            "._pattern.PatternValidator",
            "._line.LineValidator",
            "._colorssrc.ColorssrcValidator",
            "._colors.ColorsValidator",
        ],
    )
