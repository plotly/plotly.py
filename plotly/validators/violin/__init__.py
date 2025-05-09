import sys
from _plotly_utils.importers import relative_import

__all__, __getattr__, __dir__ = relative_import(
    __name__,
    [],
    [
        "._zorder.ZorderValidator",
        "._ysrc.YsrcValidator",
        "._yhoverformat.YhoverformatValidator",
        "._yaxis.YaxisValidator",
        "._y0.Y0Validator",
        "._y.YValidator",
        "._xsrc.XsrcValidator",
        "._xhoverformat.XhoverformatValidator",
        "._xaxis.XaxisValidator",
        "._x0.X0Validator",
        "._x.XValidator",
        "._width.WidthValidator",
        "._visible.VisibleValidator",
        "._unselected.UnselectedValidator",
        "._uirevision.UirevisionValidator",
        "._uid.UidValidator",
        "._textsrc.TextsrcValidator",
        "._text.TextValidator",
        "._stream.StreamValidator",
        "._spanmode.SpanmodeValidator",
        "._span.SpanValidator",
        "._side.SideValidator",
        "._showlegend.ShowlegendValidator",
        "._selectedpoints.SelectedpointsValidator",
        "._selected.SelectedValidator",
        "._scalemode.ScalemodeValidator",
        "._scalegroup.ScalegroupValidator",
        "._quartilemethod.QuartilemethodValidator",
        "._points.PointsValidator",
        "._pointpos.PointposValidator",
        "._orientation.OrientationValidator",
        "._opacity.OpacityValidator",
        "._offsetgroup.OffsetgroupValidator",
        "._name.NameValidator",
        "._metasrc.MetasrcValidator",
        "._meta.MetaValidator",
        "._meanline.MeanlineValidator",
        "._marker.MarkerValidator",
        "._line.LineValidator",
        "._legendwidth.LegendwidthValidator",
        "._legendrank.LegendrankValidator",
        "._legendgrouptitle.LegendgrouptitleValidator",
        "._legendgroup.LegendgroupValidator",
        "._legend.LegendValidator",
        "._jitter.JitterValidator",
        "._idssrc.IdssrcValidator",
        "._ids.IdsValidator",
        "._hovertextsrc.HovertextsrcValidator",
        "._hovertext.HovertextValidator",
        "._hovertemplatesrc.HovertemplatesrcValidator",
        "._hovertemplate.HovertemplateValidator",
        "._hoveron.HoveronValidator",
        "._hoverlabel.HoverlabelValidator",
        "._hoverinfosrc.HoverinfosrcValidator",
        "._hoverinfo.HoverinfoValidator",
        "._fillcolor.FillcolorValidator",
        "._customdatasrc.CustomdatasrcValidator",
        "._customdata.CustomdataValidator",
        "._box.BoxValidator",
        "._bandwidth.BandwidthValidator",
        "._alignmentgroup.AlignmentgroupValidator",
    ],
)
