import sys
from _plotly_utils.importers import relative_import

__all__, __getattr__, __dir__ = relative_import(
    __name__,
    [],
    [
        "._thickness.ThicknessValidator",
        "._templateitemname.TemplateitemnameValidator",
        "._range.RangeValidator",
        "._name.NameValidator",
        "._line.LineValidator",
        "._color.ColorValidator",
    ],
)
