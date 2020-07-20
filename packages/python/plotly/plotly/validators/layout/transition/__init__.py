import sys

if sys.version_info < (3, 7):
    from ._ordering import OrderingValidator
    from ._easing import EasingValidator
    from ._duration import DurationValidator
else:
    from _plotly_utils.importers import relative_import

    __all__, __getattr__, __dir__ = relative_import(
        __name__,
        [],
        [
            "._ordering.OrderingValidator",
            "._easing.EasingValidator",
            "._duration.DurationValidator",
        ],
    )
