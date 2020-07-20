import sys

if sys.version_info < (3, 7):
    from ._data import Data
    from ._layout import Layout
    from . import data
else:
    from _plotly_utils.importers import relative_import

    __all__, __getattr__, __dir__ = relative_import(
        __name__, [".data"], ["._data.Data", "._layout.Layout"]
    )
