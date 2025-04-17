import sys
from _plotly_utils.importers import relative_import

__all__, __getattr__, __dir__ = relative_import(
    __name__,
    [],
    [
        "._visible.VisibleValidator",
        "._tickwidth.TickwidthValidator",
        "._tickvalssrc.TickvalssrcValidator",
        "._tickvals.TickvalsValidator",
        "._ticksuffix.TicksuffixValidator",
        "._ticks.TicksValidator",
        "._tickprefix.TickprefixValidator",
        "._ticklen.TicklenValidator",
        "._tickformat.TickformatValidator",
        "._tickfont.TickfontValidator",
        "._tickcolor.TickcolorValidator",
        "._showticksuffix.ShowticksuffixValidator",
        "._showtickprefix.ShowtickprefixValidator",
        "._showticklabels.ShowticklabelsValidator",
        "._showline.ShowlineValidator",
        "._showgrid.ShowgridValidator",
        "._linewidth.LinewidthValidator",
        "._linecolor.LinecolorValidator",
        "._layer.LayerValidator",
        "._labelalias.LabelaliasValidator",
        "._hoverformat.HoverformatValidator",
        "._gridwidth.GridwidthValidator",
        "._griddash.GriddashValidator",
        "._gridcolor.GridcolorValidator",
        "._color.ColorValidator",
    ],
)
