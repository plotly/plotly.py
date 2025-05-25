import sys
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ._text import TextValidator
    from ._font import FontValidator
    from ._align import AlignValidator
else:
    from _plotly_utils.importers import relative_import

    __all__, __getattr__, __dir__ = relative_import(
        __name__,
        [],
        ["._text.TextValidator", "._font.FontValidator", "._align.AlignValidator"],
    )
