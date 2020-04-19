import sys

if sys.version_info < (3, 7):
    from ._roll import RollValidator
    from ._lon import LonValidator
    from ._lat import LatValidator
else:
    from _plotly_utils.importers import relative_import

    __all__, __getattr__, __dir__ = relative_import(
        __name__,
        [],
        ["._roll.RollValidator", "._lon.LonValidator", "._lat.LatValidator"],
    )
