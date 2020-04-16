import sys

if sys.version_info < (3, 7):
    from ._value import ValueValidator
    from ._thickness import ThicknessValidator
    from ._line import LineValidator
else:
    from _plotly_utils.importers import relative_import

    __all__, __getattr__, __dir__ = relative_import(
        __name__,
        [],
        [
            "._value.ValueValidator",
            "._thickness.ThicknessValidator",
            "._line.LineValidator",
        ],
    )
