import sys
from _plotly_utils.importers import relative_import

__all__, __getattr__, __dir__ = relative_import(
    __name__,
    [],
    [
        "._width.WidthValidator",
        "._visible.VisibleValidator",
        "._valueminus.ValueminusValidator",
        "._value.ValueValidator",
        "._type.TypeValidator",
        "._tracerefminus.TracerefminusValidator",
        "._traceref.TracerefValidator",
        "._thickness.ThicknessValidator",
        "._symmetric.SymmetricValidator",
        "._color.ColorValidator",
        "._arraysrc.ArraysrcValidator",
        "._arrayminussrc.ArrayminussrcValidator",
        "._arrayminus.ArrayminusValidator",
        "._array.ArrayValidator",
    ],
)
