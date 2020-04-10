import sys

if sys.version_info < (3, 7):
    from ._surface import Surface
    from ._stream import Stream
    from ._spaceframe import Spaceframe
    from ._slices import Slices
    from ._lightposition import Lightposition
    from ._lighting import Lighting
    from ._hoverlabel import Hoverlabel
    from ._contour import Contour
    from ._colorbar import ColorBar
    from ._caps import Caps
    from . import slices
    from . import hoverlabel
    from . import colorbar
    from . import caps
else:
    from _plotly_utils.importers import relative_import

    __all__, __getattr__ = relative_import(
        __name__,
        [".slices", ".hoverlabel", ".colorbar", ".caps"],
        [
            "._surface.Surface",
            "._stream.Stream",
            "._spaceframe.Spaceframe",
            "._slices.Slices",
            "._lightposition.Lightposition",
            "._lighting.Lighting",
            "._hoverlabel.Hoverlabel",
            "._contour.Contour",
            "._colorbar.ColorBar",
            "._caps.Caps",
        ],
    )
