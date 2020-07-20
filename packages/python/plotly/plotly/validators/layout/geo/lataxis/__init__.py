import sys

if sys.version_info < (3, 7):
    from ._tick0 import Tick0Validator
    from ._showgrid import ShowgridValidator
    from ._range import RangeValidator
    from ._gridwidth import GridwidthValidator
    from ._gridcolor import GridcolorValidator
    from ._dtick import DtickValidator
else:
    from _plotly_utils.importers import relative_import

    __all__, __getattr__, __dir__ = relative_import(
        __name__,
        [],
        [
            "._tick0.Tick0Validator",
            "._showgrid.ShowgridValidator",
            "._range.RangeValidator",
            "._gridwidth.GridwidthValidator",
            "._gridcolor.GridcolorValidator",
            "._dtick.DtickValidator",
        ],
    )
