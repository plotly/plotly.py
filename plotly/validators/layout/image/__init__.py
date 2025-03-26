import sys
from _plotly_utils.importers import relative_import

__all__, __getattr__, __dir__ = relative_import(
    __name__,
    [],
    [
        "._yref.YrefValidator",
        "._yanchor.YanchorValidator",
        "._y.YValidator",
        "._xref.XrefValidator",
        "._xanchor.XanchorValidator",
        "._x.XValidator",
        "._visible.VisibleValidator",
        "._templateitemname.TemplateitemnameValidator",
        "._source.SourceValidator",
        "._sizing.SizingValidator",
        "._sizey.SizeyValidator",
        "._sizex.SizexValidator",
        "._opacity.OpacityValidator",
        "._name.NameValidator",
        "._layer.LayerValidator",
    ],
)
