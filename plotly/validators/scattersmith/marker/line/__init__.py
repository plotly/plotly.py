import sys
from _plotly_utils.importers import relative_import

__all__, __getattr__, __dir__ = relative_import(
    __name__,
    [],
    [
        "._widthsrc.WidthsrcValidator",
        "._width.WidthValidator",
        "._reversescale.ReversescaleValidator",
        "._colorsrc.ColorsrcValidator",
        "._colorscale.ColorscaleValidator",
        "._coloraxis.ColoraxisValidator",
        "._color.ColorValidator",
        "._cmin.CminValidator",
        "._cmid.CmidValidator",
        "._cmax.CmaxValidator",
        "._cauto.CautoValidator",
        "._autocolorscale.AutocolorscaleValidator",
    ],
)
