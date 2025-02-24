import sys
from _plotly_utils.importers import relative_import

__all__, __getattr__, __dir__ = relative_import(
    __name__,
    [".colorbar", ".hoverlabel", ".legendgrouptitle"],
    [
        "._colorbar.ColorBar",
        "._hoverlabel.Hoverlabel",
        "._legendgrouptitle.Legendgrouptitle",
        "._lighting.Lighting",
        "._lightposition.Lightposition",
        "._stream.Stream",
    ],
)
