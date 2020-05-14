import sys

if sys.version_info < (3, 7):
    from ._caps import Caps
    from ._colorbar import ColorBar
    from ._contour import Contour
    from ._hoverlabel import Hoverlabel
    from ._lighting import Lighting
    from ._lightposition import Lightposition
    from ._slices import Slices
    from ._spaceframe import Spaceframe
    from ._stream import Stream
    from ._surface import Surface
    from . import caps
    from . import colorbar
    from . import hoverlabel
    from . import slices
else:
    from _plotly_utils.importers import relative_import

    __all__, __getattr__, __dir__ = relative_import(
        __name__,
        [".caps", ".colorbar", ".hoverlabel", ".slices"],
        [
            "._caps.Caps",
            "._colorbar.ColorBar",
            "._contour.Contour",
            "._hoverlabel.Hoverlabel",
            "._lighting.Lighting",
            "._lightposition.Lightposition",
            "._slices.Slices",
            "._spaceframe.Spaceframe",
            "._stream.Stream",
            "._surface.Surface",
        ],
    )
