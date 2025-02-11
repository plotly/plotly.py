import sys
from _plotly_utils.importers import relative_import

__all__, __getattr__, __dir__ = relative_import(
    __name__,
    [],
    [
        "._uirevision.UirevisionValidator",
        "._sum.SumValidator",
        "._domain.DomainValidator",
        "._caxis.CaxisValidator",
        "._bgcolor.BgcolorValidator",
        "._baxis.BaxisValidator",
        "._aaxis.AaxisValidator",
    ],
)
