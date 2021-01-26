import sys

if sys.version_info < (3, 7):
    from ._width import WidthValidator
    from ._dashsrc import DashsrcValidator
    from ._dash import DashValidator
else:
    from _plotly_utils.importers import relative_import

    __all__, __getattr__, __dir__ = relative_import(
        __name__,
        [],
        [
            "._width.WidthValidator",
            "._dashsrc.DashsrcValidator",
            "._dash.DashValidator",
        ],
    )
