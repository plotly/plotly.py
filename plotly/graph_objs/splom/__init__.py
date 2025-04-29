import sys
from _plotly_utils.importers import relative_import

__all__, __getattr__, __dir__ = relative_import(
    __name__,
    [
        ".dimension",
        ".hoverlabel",
        ".legendgrouptitle",
        ".marker",
        ".selected",
        ".unselected",
    ],
    [
        "._diagonal.Diagonal",
        "._dimension.Dimension",
        "._hoverlabel.Hoverlabel",
        "._legendgrouptitle.Legendgrouptitle",
        "._marker.Marker",
        "._selected.Selected",
        "._stream.Stream",
        "._unselected.Unselected",
    ],
)
