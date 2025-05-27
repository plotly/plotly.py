import sys
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ._line import LineValidator
    from ._fillcolor import FillcolorValidator
else:
    from _plotly_utils.importers import relative_import

    __all__, __getattr__, __dir__ = relative_import(
        __name__, [], ["._line.LineValidator", "._fillcolor.FillcolorValidator"]
    )
