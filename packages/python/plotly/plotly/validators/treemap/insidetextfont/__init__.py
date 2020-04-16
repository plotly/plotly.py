import sys

if sys.version_info < (3, 7):
    from ._sizesrc import SizesrcValidator
    from ._size import SizeValidator
    from ._familysrc import FamilysrcValidator
    from ._family import FamilyValidator
    from ._colorsrc import ColorsrcValidator
    from ._color import ColorValidator
else:
    from _plotly_utils.importers import relative_import

    __all__, __getattr__, __dir__ = relative_import(
        __name__,
        [],
        [
            "._sizesrc.SizesrcValidator",
            "._size.SizeValidator",
            "._familysrc.FamilysrcValidator",
            "._family.FamilyValidator",
            "._colorsrc.ColorsrcValidator",
            "._color.ColorValidator",
        ],
    )
