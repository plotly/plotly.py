import sys
from _plotly_utils.importers import relative_import

__all__, __getattr__, __dir__ = relative_import(
    __name__,
    [],
    [
        "._symbol.SymbolValidator",
        "._size.SizeValidator",
        "._outliercolor.OutliercolorValidator",
        "._opacity.OpacityValidator",
        "._line.LineValidator",
        "._color.ColorValidator",
        "._angle.AngleValidator",
    ],
)
