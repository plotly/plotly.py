import sys
from _plotly_utils.importers import relative_import

__all__, __getattr__, __dir__ = relative_import(
    __name__,
    [],
    [
        "._yanchor.YanchorValidator",
        "._y.YValidator",
        "._xanchor.XanchorValidator",
        "._x.XValidator",
        "._visible.VisibleValidator",
        "._type.TypeValidator",
        "._templateitemname.TemplateitemnameValidator",
        "._showactive.ShowactiveValidator",
        "._pad.PadValidator",
        "._name.NameValidator",
        "._font.FontValidator",
        "._direction.DirectionValidator",
        "._buttondefaults.ButtondefaultsValidator",
        "._buttons.ButtonsValidator",
        "._borderwidth.BorderwidthValidator",
        "._bordercolor.BordercolorValidator",
        "._bgcolor.BgcolorValidator",
        "._active.ActiveValidator",
    ],
)
