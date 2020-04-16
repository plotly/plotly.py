import sys

if sys.version_info < (3, 7):
    from ._visible import VisibleValidator
    from ._ticksuffix import TicksuffixValidator
    from ._tickorientation import TickorientationValidator
    from ._ticklen import TicklenValidator
    from ._tickcolor import TickcolorValidator
    from ._showticklabels import ShowticklabelsValidator
    from ._showline import ShowlineValidator
    from ._range import RangeValidator
    from ._orientation import OrientationValidator
    from ._endpadding import EndpaddingValidator
    from ._domain import DomainValidator
else:
    from _plotly_utils.importers import relative_import

    __all__, __getattr__, __dir__ = relative_import(
        __name__,
        [],
        [
            "._visible.VisibleValidator",
            "._ticksuffix.TicksuffixValidator",
            "._tickorientation.TickorientationValidator",
            "._ticklen.TicklenValidator",
            "._tickcolor.TickcolorValidator",
            "._showticklabels.ShowticklabelsValidator",
            "._showline.ShowlineValidator",
            "._range.RangeValidator",
            "._orientation.OrientationValidator",
            "._endpadding.EndpaddingValidator",
            "._domain.DomainValidator",
        ],
    )
