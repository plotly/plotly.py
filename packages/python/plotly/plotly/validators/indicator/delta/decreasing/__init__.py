import sys

if sys.version_info < (3, 7):
    from ._symbol import SymbolValidator
    from ._color import ColorValidator
else:
    from _plotly_utils.importers import relative_import

    __all__, __getattr__, __dir__ = relative_import(
        __name__, [], ["._symbol.SymbolValidator", "._color.ColorValidator"]
    )
