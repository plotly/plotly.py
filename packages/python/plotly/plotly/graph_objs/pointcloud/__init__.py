import sys

if sys.version_info < (3, 7):
    from ._hoverlabel import Hoverlabel
    from ._marker import Marker
    from ._stream import Stream
    from . import hoverlabel
    from . import marker
else:
    from _plotly_utils.importers import relative_import

    __all__, __getattr__, __dir__ = relative_import(
        __name__,
        [".hoverlabel", ".marker"],
        ["._hoverlabel.Hoverlabel", "._marker.Marker", "._stream.Stream"],
    )
