import sys
from _plotly_utils.importers import relative_import

__all__, __getattr__, __dir__ = relative_import(
    __name__,
    [],
    [
        "._yshift.YshiftValidator",
        "._yref.YrefValidator",
        "._yclick.YclickValidator",
        "._yanchor.YanchorValidator",
        "._y.YValidator",
        "._xshift.XshiftValidator",
        "._xref.XrefValidator",
        "._xclick.XclickValidator",
        "._xanchor.XanchorValidator",
        "._x.XValidator",
        "._width.WidthValidator",
        "._visible.VisibleValidator",
        "._valign.ValignValidator",
        "._textangle.TextangleValidator",
        "._text.TextValidator",
        "._templateitemname.TemplateitemnameValidator",
        "._startstandoff.StartstandoffValidator",
        "._startarrowsize.StartarrowsizeValidator",
        "._startarrowhead.StartarrowheadValidator",
        "._standoff.StandoffValidator",
        "._showarrow.ShowarrowValidator",
        "._opacity.OpacityValidator",
        "._name.NameValidator",
        "._hovertext.HovertextValidator",
        "._hoverlabel.HoverlabelValidator",
        "._height.HeightValidator",
        "._font.FontValidator",
        "._clicktoshow.ClicktoshowValidator",
        "._captureevents.CaptureeventsValidator",
        "._borderwidth.BorderwidthValidator",
        "._borderpad.BorderpadValidator",
        "._bordercolor.BordercolorValidator",
        "._bgcolor.BgcolorValidator",
        "._ayref.AyrefValidator",
        "._ay.AyValidator",
        "._axref.AxrefValidator",
        "._ax.AxValidator",
        "._arrowwidth.ArrowwidthValidator",
        "._arrowsize.ArrowsizeValidator",
        "._arrowside.ArrowsideValidator",
        "._arrowhead.ArrowheadValidator",
        "._arrowcolor.ArrowcolorValidator",
        "._align.AlignValidator",
    ],
)
