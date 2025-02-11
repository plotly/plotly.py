import sys
from _plotly_utils.importers import relative_import

__all__, __getattr__, __dir__ = relative_import(
    __name__,
    [],
    [
        "._yref.YrefValidator",
        "._y1.Y1Validator",
        "._y0.Y0Validator",
        "._xref.XrefValidator",
        "._x1.X1Validator",
        "._x0.X0Validator",
        "._type.TypeValidator",
        "._templateitemname.TemplateitemnameValidator",
        "._path.PathValidator",
        "._opacity.OpacityValidator",
        "._name.NameValidator",
        "._line.LineValidator",
    ],
)
