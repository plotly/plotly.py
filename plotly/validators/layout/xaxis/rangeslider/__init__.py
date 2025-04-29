import sys
from _plotly_utils.importers import relative_import

__all__, __getattr__, __dir__ = relative_import(
    __name__,
    [],
    [
        "._yaxis.YaxisValidator",
        "._visible.VisibleValidator",
        "._thickness.ThicknessValidator",
        "._range.RangeValidator",
        "._borderwidth.BorderwidthValidator",
        "._bordercolor.BordercolorValidator",
        "._bgcolor.BgcolorValidator",
        "._autorange.AutorangeValidator",
    ],
)
