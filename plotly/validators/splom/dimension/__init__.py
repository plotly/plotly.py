import sys
from _plotly_utils.importers import relative_import

__all__, __getattr__, __dir__ = relative_import(
    __name__,
    [],
    [
        "._visible.VisibleValidator",
        "._valuessrc.ValuessrcValidator",
        "._values.ValuesValidator",
        "._templateitemname.TemplateitemnameValidator",
        "._name.NameValidator",
        "._label.LabelValidator",
        "._axis.AxisValidator",
    ],
)
