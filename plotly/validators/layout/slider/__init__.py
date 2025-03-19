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
        "._transition.TransitionValidator",
        "._tickwidth.TickwidthValidator",
        "._ticklen.TicklenValidator",
        "._tickcolor.TickcolorValidator",
        "._templateitemname.TemplateitemnameValidator",
        "._stepdefaults.StepdefaultsValidator",
        "._steps.StepsValidator",
        "._pad.PadValidator",
        "._name.NameValidator",
        "._minorticklen.MinorticklenValidator",
        "._lenmode.LenmodeValidator",
        "._len.LenValidator",
        "._font.FontValidator",
        "._currentvalue.CurrentvalueValidator",
        "._borderwidth.BorderwidthValidator",
        "._bordercolor.BordercolorValidator",
        "._bgcolor.BgcolorValidator",
        "._activebgcolor.ActivebgcolorValidator",
        "._active.ActiveValidator",
    ],
)
