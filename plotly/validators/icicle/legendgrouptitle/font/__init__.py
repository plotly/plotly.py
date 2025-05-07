import sys
from _plotly_utils.importers import relative_import

__all__, __getattr__, __dir__ = relative_import(
    __name__,
    [],
    [
        "._weight.WeightValidator",
        "._variant.VariantValidator",
        "._textcase.TextcaseValidator",
        "._style.StyleValidator",
        "._size.SizeValidator",
        "._shadow.ShadowValidator",
        "._lineposition.LinepositionValidator",
        "._family.FamilyValidator",
        "._color.ColorValidator",
    ],
)
