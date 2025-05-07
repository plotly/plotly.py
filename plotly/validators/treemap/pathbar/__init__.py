import sys
from _plotly_utils.importers import relative_import

__all__, __getattr__, __dir__ = relative_import(
    __name__,
    [],
    [
        "._visible.VisibleValidator",
        "._thickness.ThicknessValidator",
        "._textfont.TextfontValidator",
        "._side.SideValidator",
        "._edgeshape.EdgeshapeValidator",
    ],
)
