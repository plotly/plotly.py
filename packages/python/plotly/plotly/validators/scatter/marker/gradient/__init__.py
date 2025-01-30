import sys
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ._typesrc import TypesrcValidator
    from ._type import TypeValidator
    from ._colorsrc import ColorsrcValidator
    from ._color import ColorValidator
else:
    from _plotly_utils.importers import relative_import

    __all__, __getattr__, __dir__ = relative_import(
        __name__,
        [],
        [
            "._typesrc.TypesrcValidator",
            "._type.TypeValidator",
            "._colorsrc.ColorsrcValidator",
            "._color.ColorValidator",
        ],
    )
