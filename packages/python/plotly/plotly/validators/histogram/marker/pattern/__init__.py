import sys

if sys.version_info < (3, 7):
    from ._soliditysrc import SoliditysrcValidator
    from ._solidity import SolidityValidator
    from ._sizesrc import SizesrcValidator
    from ._size import SizeValidator
    from ._shapesrc import ShapesrcValidator
    from ._shape import ShapeValidator
    from ._bgcolorsrc import BgcolorsrcValidator
    from ._bgcolor import BgcolorValidator
else:
    from _plotly_utils.importers import relative_import

    __all__, __getattr__, __dir__ = relative_import(
        __name__,
        [],
        [
            "._soliditysrc.SoliditysrcValidator",
            "._solidity.SolidityValidator",
            "._sizesrc.SizesrcValidator",
            "._size.SizeValidator",
            "._shapesrc.ShapesrcValidator",
            "._shape.ShapeValidator",
            "._bgcolorsrc.BgcolorsrcValidator",
            "._bgcolor.BgcolorValidator",
        ],
    )
