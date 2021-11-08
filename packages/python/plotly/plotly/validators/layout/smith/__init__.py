import sys

if sys.version_info < (3, 7):
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
