import sys

if sys.version_info < (3, 7):
    from ._title import Title
    from ._font import Font
    from . import title
else:
    from _plotly_utils.importers import relative_import

    __all__, __getattr__ = relative_import(
        __name__, [".title"], ["._title.Title", "._font.Font"]
    )
