import sys

if sys.version_info < (3, 7):
    from ._increasing import Increasing
    from ._font import Font
    from ._decreasing import Decreasing
else:
    from _plotly_utils.importers import relative_import

    __all__, __getattr__, __dir__ = relative_import(
        __name__,
        [],
        ["._increasing.Increasing", "._font.Font", "._decreasing.Decreasing"],
    )
