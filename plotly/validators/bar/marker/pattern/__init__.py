import sys
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
        "._fillmode.FillmodeValidator",
        "._fgopacity.FgopacityValidator",
        "._fgcolorsrc.FgcolorsrcValidator",
        "._fgcolor.FgcolorValidator",
        "._bgcolorsrc.BgcolorsrcValidator",
        "._bgcolor.BgcolorValidator",
    ],
)
