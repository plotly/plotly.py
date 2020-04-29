import sys

if sys.version_info < (3, 7):
    from ._font import Font
    from ._title import Title
    from . import title
else:
    from _plotly_utils.importers import relative_import

    __all__, __getattr__, __dir__ = relative_import(
        __name__, [".title"], ["._font.Font", "._title.Title"]
    )
