import sys
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ._visible import VisibleValidator
    from ._thickness import ThicknessValidator
    from ._textfont import TextfontValidator
    from ._side import SideValidator
    from ._edgeshape import EdgeshapeValidator
else:
    from _plotly_utils.importers import relative_import

    __all__, __getattr__, __dir__ = relative_import(
        __name__,
        [],
        [
            "._visible.VisibleValidator",
            "._thickness.ThicknessValidator",
            "._textfont.TextfontValidator",
            "._side.SideValidator",
            "._edgeshape.EdgeshapeValidator",
        ],
    )
