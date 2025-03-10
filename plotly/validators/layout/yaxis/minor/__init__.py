import sys
from _plotly_utils.importers import relative_import

__all__, __getattr__, __dir__ = relative_import(
    __name__,
    [],
    [
        "._tickwidth.TickwidthValidator",
        "._tickvalssrc.TickvalssrcValidator",
        "._tickvals.TickvalsValidator",
        "._ticks.TicksValidator",
        "._tickmode.TickmodeValidator",
        "._ticklen.TicklenValidator",
        "._tickcolor.TickcolorValidator",
        "._tick0.Tick0Validator",
        "._showgrid.ShowgridValidator",
        "._nticks.NticksValidator",
        "._gridwidth.GridwidthValidator",
        "._griddash.GriddashValidator",
        "._gridcolor.GridcolorValidator",
        "._dtick.DtickValidator",
    ],
)
