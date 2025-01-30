import sys
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ._font import FontValidator
    from ._bordercolor import BordercolorValidator
    from ._bgcolor import BgcolorValidator
else:
    from _plotly_utils.importers import relative_import

    __all__, __getattr__, __dir__ = relative_import(
        __name__,
        [],
        [
            "._font.FontValidator",
            "._bordercolor.BordercolorValidator",
            "._bgcolor.BgcolorValidator",
        ],
    )
