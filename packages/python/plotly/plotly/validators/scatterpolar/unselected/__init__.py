import sys
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ._textfont import TextfontValidator
    from ._marker import MarkerValidator
else:
    from _plotly_utils.importers import relative_import

    __all__, __getattr__, __dir__ = relative_import(
        __name__, [], ["._textfont.TextfontValidator", "._marker.MarkerValidator"]
    )
