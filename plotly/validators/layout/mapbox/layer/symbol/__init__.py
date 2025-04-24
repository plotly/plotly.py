import sys
from _plotly_utils.importers import relative_import

__all__, __getattr__, __dir__ = relative_import(
    __name__,
    [],
    [
        "._textposition.TextpositionValidator",
        "._textfont.TextfontValidator",
        "._text.TextValidator",
        "._placement.PlacementValidator",
        "._iconsize.IconsizeValidator",
        "._icon.IconValidator",
    ],
)
