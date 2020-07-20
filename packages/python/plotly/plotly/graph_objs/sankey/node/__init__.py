import sys

if sys.version_info < (3, 7):
    from ._hoverlabel import Hoverlabel
    from ._line import Line
    from . import hoverlabel
else:
    from _plotly_utils.importers import relative_import

    __all__, __getattr__, __dir__ = relative_import(
        __name__, [".hoverlabel"], ["._hoverlabel.Hoverlabel", "._line.Line"]
    )
