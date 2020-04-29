import sys

if sys.version_info < (3, 7):
    from ._decreasing import Decreasing
    from ._font import Font
    from ._increasing import Increasing
else:
    from _plotly_utils.importers import relative_import

    __all__, __getattr__, __dir__ = relative_import(
        __name__,
        [],
        ["._decreasing.Decreasing", "._font.Font", "._increasing.Increasing"],
    )
