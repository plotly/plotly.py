import sys

if sys.version_info < (3, 7):
    from ._layout import Layout
    from ._data import Data
    from . import data
else:
    from _plotly_utils.importers import relative_import

    __all__, __getattr__ = relative_import(
        __name__, [".data"], ["._layout.Layout", "._data.Data"]
    )
