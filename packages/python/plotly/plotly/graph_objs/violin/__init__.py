import sys

if sys.version_info < (3, 7):
    from ._box import Box
    from ._hoverlabel import Hoverlabel
    from ._line import Line
    from ._marker import Marker
    from ._meanline import Meanline
    from ._selected import Selected
    from ._stream import Stream
    from ._unselected import Unselected
    from . import box
    from . import hoverlabel
    from . import marker
    from . import selected
    from . import unselected
else:
    from _plotly_utils.importers import relative_import

    __all__, __getattr__, __dir__ = relative_import(
        __name__,
        [".box", ".hoverlabel", ".marker", ".selected", ".unselected"],
        [
            "._box.Box",
            "._hoverlabel.Hoverlabel",
            "._line.Line",
            "._marker.Marker",
            "._meanline.Meanline",
            "._selected.Selected",
            "._stream.Stream",
            "._unselected.Unselected",
        ],
    )
