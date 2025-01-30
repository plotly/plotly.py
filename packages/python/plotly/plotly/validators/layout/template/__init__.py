import sys
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ._layout import LayoutValidator
    from ._data import DataValidator
else:
    from _plotly_utils.importers import relative_import

    __all__, __getattr__, __dir__ = relative_import(
        __name__, [], ["._layout.LayoutValidator", "._data.DataValidator"]
    )
