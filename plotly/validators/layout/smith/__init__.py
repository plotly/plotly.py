import sys
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ._realaxis import RealaxisValidator
    from ._imaginaryaxis import ImaginaryaxisValidator
    from ._domain import DomainValidator
    from ._bgcolor import BgcolorValidator
else:
    from _plotly_utils.importers import relative_import

    __all__, __getattr__, __dir__ = relative_import(
        __name__,
        [],
        [
            "._realaxis.RealaxisValidator",
            "._imaginaryaxis.ImaginaryaxisValidator",
            "._domain.DomainValidator",
            "._bgcolor.BgcolorValidator",
        ],
    )
