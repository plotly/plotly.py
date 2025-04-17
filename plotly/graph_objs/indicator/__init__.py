import sys
from _plotly_utils.importers import relative_import

__all__, __getattr__, __dir__ = relative_import(
    __name__,
    [".delta", ".gauge", ".legendgrouptitle", ".number", ".title"],
    [
        "._delta.Delta",
        "._domain.Domain",
        "._gauge.Gauge",
        "._legendgrouptitle.Legendgrouptitle",
        "._number.Number",
        "._stream.Stream",
        "._title.Title",
    ],
)
