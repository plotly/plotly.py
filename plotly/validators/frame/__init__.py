import sys
from _plotly_utils.importers import relative_import

__all__, __getattr__, __dir__ = relative_import(
    __name__,
    [],
    [
        "._traces.TracesValidator",
        "._name.NameValidator",
        "._layout.LayoutValidator",
        "._group.GroupValidator",
        "._data.DataValidator",
        "._baseframe.BaseframeValidator",
    ],
)
