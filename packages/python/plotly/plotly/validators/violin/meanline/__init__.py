import sys
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ._width import WidthValidator
    from ._visible import VisibleValidator
    from ._color import ColorValidator
else:
    from _plotly_utils.importers import relative_import

    __all__, __getattr__, __dir__ = relative_import(
        __name__,
        [],
        [
            "._width.WidthValidator",
            "._visible.VisibleValidator",
            "._color.ColorValidator",
        ],
    )
