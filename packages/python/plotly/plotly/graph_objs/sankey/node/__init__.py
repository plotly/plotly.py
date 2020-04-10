import sys

if sys.version_info < (3, 7):
    from ._line import Line
    from ._hoverlabel import Hoverlabel
    from . import hoverlabel
else:
    from _plotly_utils.importers import relative_import

    __all__, __getattr__ = relative_import(
        __name__, [".hoverlabel"], ["._line.Line", "._hoverlabel.Hoverlabel"]
    )
