import sys
from _plotly_utils.importers import relative_import

__all__, __getattr__, __dir__ = relative_import(
    __name__,
    [".caps", ".colorbar", ".hoverlabel", ".legendgrouptitle", ".slices"],
    [
        "._caps.Caps",
        "._colorbar.ColorBar",
        "._contour.Contour",
        "._hoverlabel.Hoverlabel",
        "._legendgrouptitle.Legendgrouptitle",
        "._lighting.Lighting",
        "._lightposition.Lightposition",
        "._slices.Slices",
        "._spaceframe.Spaceframe",
        "._stream.Stream",
        "._surface.Surface",
    ],
)
