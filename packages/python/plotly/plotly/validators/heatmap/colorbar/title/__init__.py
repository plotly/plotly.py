import sys

if sys.version_info < (3, 7):
    from ._text import TextValidator
    from ._side import SideValidator
    from ._font import FontValidator
else:
    from _plotly_utils.importers import relative_import

    __all__, __getattr__, __dir__ = relative_import(
        __name__,
        [],
        ["._text.TextValidator", "._side.SideValidator", "._font.FontValidator"],
    )
