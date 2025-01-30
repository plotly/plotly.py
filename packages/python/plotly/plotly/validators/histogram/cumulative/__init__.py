import sys
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ._enabled import EnabledValidator
    from ._direction import DirectionValidator
    from ._currentbin import CurrentbinValidator
else:
    from _plotly_utils.importers import relative_import

    __all__, __getattr__, __dir__ = relative_import(
        __name__,
        [],
        [
            "._enabled.EnabledValidator",
            "._direction.DirectionValidator",
            "._currentbin.CurrentbinValidator",
        ],
    )
