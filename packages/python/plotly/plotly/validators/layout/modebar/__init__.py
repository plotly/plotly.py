import sys

if sys.version_info < (3, 7):
    from ._uirevision import UirevisionValidator
    from ._orientation import OrientationValidator
    from ._color import ColorValidator
    from ._bgcolor import BgcolorValidator
    from ._activecolor import ActivecolorValidator
else:
    from _plotly_utils.importers import relative_import

    __all__, __getattr__, __dir__ = relative_import(
        __name__,
        [],
        [
            "._uirevision.UirevisionValidator",
            "._orientation.OrientationValidator",
            "._color.ColorValidator",
            "._bgcolor.BgcolorValidator",
            "._activecolor.ActivecolorValidator",
        ],
    )
