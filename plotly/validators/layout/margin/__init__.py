import sys
from _plotly_utils.importers import relative_import

__all__, __getattr__, __dir__ = relative_import(
    __name__,
    [],
    [
        "._t.TValidator",
        "._r.RValidator",
        "._pad.PadValidator",
        "._l.LValidator",
        "._b.BValidator",
        "._autoexpand.AutoexpandValidator",
    ],
)
