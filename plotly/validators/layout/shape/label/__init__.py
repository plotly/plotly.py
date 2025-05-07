import sys
from _plotly_utils.importers import relative_import

__all__, __getattr__, __dir__ = relative_import(
    __name__,
    [],
    [
        "._yanchor.YanchorValidator",
        "._xanchor.XanchorValidator",
        "._texttemplate.TexttemplateValidator",
        "._textposition.TextpositionValidator",
        "._textangle.TextangleValidator",
        "._text.TextValidator",
        "._padding.PaddingValidator",
        "._font.FontValidator",
    ],
)
