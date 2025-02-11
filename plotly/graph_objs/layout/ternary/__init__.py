import sys
from _plotly_utils.importers import relative_import

__all__, __getattr__, __dir__ = relative_import(
    __name__,
    [".aaxis", ".baxis", ".caxis"],
    ["._aaxis.Aaxis", "._baxis.Baxis", "._caxis.Caxis", "._domain.Domain"],
)
