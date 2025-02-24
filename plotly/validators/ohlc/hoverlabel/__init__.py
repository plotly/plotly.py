import sys
from _plotly_utils.importers import relative_import

__all__, __getattr__, __dir__ = relative_import(
    __name__,
    [],
    [
        "._split.SplitValidator",
        "._namelengthsrc.NamelengthsrcValidator",
        "._namelength.NamelengthValidator",
        "._font.FontValidator",
        "._bordercolorsrc.BordercolorsrcValidator",
        "._bordercolor.BordercolorValidator",
        "._bgcolorsrc.BgcolorsrcValidator",
        "._bgcolor.BgcolorValidator",
        "._alignsrc.AlignsrcValidator",
        "._align.AlignValidator",
    ],
)
