import sys
from _plotly_utils.importers import relative_import

__all__, __getattr__, __dir__ = relative_import(
    __name__,
    [],
    [
        "._xanchor.XanchorValidator",
        "._visible.VisibleValidator",
        "._suffix.SuffixValidator",
        "._prefix.PrefixValidator",
        "._offset.OffsetValidator",
        "._font.FontValidator",
    ],
)
