import sys
from _plotly_utils.importers import relative_import

__all__, __getattr__, __dir__ = relative_import(
    __name__,
    [],
    [
        "._weightsrc.WeightsrcValidator",
        "._weight.WeightValidator",
        "._variantsrc.VariantsrcValidator",
        "._variant.VariantValidator",
        "._textcasesrc.TextcasesrcValidator",
        "._textcase.TextcaseValidator",
        "._stylesrc.StylesrcValidator",
        "._style.StyleValidator",
        "._sizesrc.SizesrcValidator",
        "._size.SizeValidator",
        "._shadowsrc.ShadowsrcValidator",
        "._shadow.ShadowValidator",
        "._linepositionsrc.LinepositionsrcValidator",
        "._lineposition.LinepositionValidator",
        "._familysrc.FamilysrcValidator",
        "._family.FamilyValidator",
        "._colorsrc.ColorsrcValidator",
        "._color.ColorValidator",
    ],
)
