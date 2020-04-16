import sys

if sys.version_info < (3, 7):
    from ._symbolsrc import SymbolsrcValidator
    from ._symbol import SymbolValidator
    from ._sizesrc import SizesrcValidator
    from ._size import SizeValidator
    from ._opacitysrc import OpacitysrcValidator
    from ._opacity import OpacityValidator
    from ._colorsrc import ColorsrcValidator
    from ._color import ColorValidator
else:
    from _plotly_utils.importers import relative_import

    __all__, __getattr__, __dir__ = relative_import(
        __name__,
        [],
        [
            "._symbolsrc.SymbolsrcValidator",
            "._symbol.SymbolValidator",
            "._sizesrc.SizesrcValidator",
            "._size.SizeValidator",
            "._opacitysrc.OpacitysrcValidator",
            "._opacity.OpacityValidator",
            "._colorsrc.ColorsrcValidator",
            "._color.ColorValidator",
        ],
    )
