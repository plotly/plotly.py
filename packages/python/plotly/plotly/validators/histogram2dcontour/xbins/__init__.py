import sys
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ._start import StartValidator
    from ._size import SizeValidator
    from ._end import EndValidator
else:
    from _plotly_utils.importers import relative_import

    __all__, __getattr__, __dir__ = relative_import(
        __name__,
        [],
        ["._start.StartValidator", "._size.SizeValidator", "._end.EndValidator"],
    )
