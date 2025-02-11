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
        "._font.FontValidator",
        "._buttondefaults.ButtondefaultsValidator",
        "._buttons.ButtonsValidator",
        "._borderwidth.BorderwidthValidator",
        "._bordercolor.BordercolorValidator",
        "._bgcolor.BgcolorValidator",
        "._activecolor.ActivecolorValidator",
    ],
)
