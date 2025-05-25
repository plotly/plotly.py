import sys
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ._width import WidthValidator
    from ._smoothing import SmoothingValidator
    from ._dash import DashValidator
    from ._color import ColorValidator
else:
    from _plotly_utils.importers import relative_import

    __all__, __getattr__, __dir__ = relative_import(
        __name__,
        [],
        [
            "._width.WidthValidator",
            "._smoothing.SmoothingValidator",
            "._dash.DashValidator",
            "._color.ColorValidator",
        ],
    )
