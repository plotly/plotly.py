import sys

if sys.version_info < (3, 7):
    from ._buttons import Buttons
    from ._font import Font
else:
    from _plotly_utils.importers import relative_import

    __all__, __getattr__, __dir__ = relative_import(
        __name__, [], ["._buttons.Buttons", "._font.Font"]
    )
