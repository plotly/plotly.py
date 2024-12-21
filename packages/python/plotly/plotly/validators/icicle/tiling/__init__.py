import sys
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ._pad import PadValidator
    from ._orientation import OrientationValidator
    from ._flip import FlipValidator
else:
    from _plotly_utils.importers import relative_import

    __all__, __getattr__, __dir__ = relative_import(
        __name__,
        [],
        [
            "._pad.PadValidator",
            "._orientation.OrientationValidator",
            "._flip.FlipValidator",
        ],
    )
