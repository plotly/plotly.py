import sys
from _plotly_utils.importers import relative_import

__all__, __getattr__, __dir__ = relative_import(
    __name__,
    [],
    [
        "._uirevision.UirevisionValidator",
        "._removesrc.RemovesrcValidator",
        "._remove.RemoveValidator",
        "._orientation.OrientationValidator",
        "._color.ColorValidator",
        "._bgcolor.BgcolorValidator",
        "._addsrc.AddsrcValidator",
        "._add.AddValidator",
        "._activecolor.ActivecolorValidator",
    ],
)
