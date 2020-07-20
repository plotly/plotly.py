import sys

if sys.version_info < (3, 7):
    from ._colorbar import ColorBar
    from ._contours import Contours
    from ._hoverlabel import Hoverlabel
    from ._lighting import Lighting
    from ._lightposition import Lightposition
    from ._stream import Stream
    from . import colorbar
    from . import contours
    from . import hoverlabel
else:
    from _plotly_utils.importers import relative_import

    __all__, __getattr__, __dir__ = relative_import(
        __name__,
        [".colorbar", ".contours", ".hoverlabel"],
        [
            "._colorbar.ColorBar",
            "._contours.Contours",
            "._hoverlabel.Hoverlabel",
            "._lighting.Lighting",
            "._lightposition.Lightposition",
            "._stream.Stream",
        ],
    )
