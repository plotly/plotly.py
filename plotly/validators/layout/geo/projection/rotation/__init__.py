import sys
from typing import TYPE_CHECKING

if TYPE_CHECKING:
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
