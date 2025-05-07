import sys
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
