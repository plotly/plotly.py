import sys

if sys.version_info < (3, 7):
    from ._namelength import NamelengthValidator
    from ._font import FontValidator
    from ._bordercolor import BordercolorValidator
    from ._bgcolor import BgcolorValidator
    from ._align import AlignValidator
else:
    from _plotly_utils.importers import relative_import

    __all__, __getattr__, __dir__ = relative_import(
        __name__,
        [],
        [
            "._namelength.NamelengthValidator",
            "._font.FontValidator",
            "._bordercolor.BordercolorValidator",
            "._bgcolor.BgcolorValidator",
            "._align.AlignValidator",
        ],
    )
