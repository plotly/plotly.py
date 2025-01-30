import sys
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ._rangemode import RangemodeValidator
    from ._range import RangeValidator
else:
    from _plotly_utils.importers import relative_import

    __all__, __getattr__, __dir__ = relative_import(
        __name__, [], ["._rangemode.RangemodeValidator", "._range.RangeValidator"]
    )
