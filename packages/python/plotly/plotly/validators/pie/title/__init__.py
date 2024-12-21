import sys
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ._text import TextValidator
    from ._position import PositionValidator
    from ._font import FontValidator
else:
    from _plotly_utils.importers import relative_import

    __all__, __getattr__, __dir__ = relative_import(
        __name__,
        [],
        [
            "._text.TextValidator",
            "._position.PositionValidator",
            "._font.FontValidator",
        ],
    )
