import sys

if sys.version_info < (3, 7):
    from ._traces import TracesValidator
    from ._name import NameValidator
    from ._layout import LayoutValidator
    from ._group import GroupValidator
    from ._data import DataValidator
    from ._baseframe import BaseframeValidator
else:
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
