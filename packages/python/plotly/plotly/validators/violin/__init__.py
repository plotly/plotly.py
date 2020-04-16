import sys

if sys.version_info < (3, 7):
    from ._ysrc import YsrcValidator
    from ._yaxis import YaxisValidator
    from ._y0 import Y0Validator
    from ._y import YValidator
    from ._xsrc import XsrcValidator
    from ._xaxis import XaxisValidator
    from ._x0 import X0Validator
    from ._x import XValidator
    from ._width import WidthValidator
    from ._visible import VisibleValidator
    from ._unselected import UnselectedValidator
    from ._uirevision import UirevisionValidator
    from ._uid import UidValidator
    from ._textsrc import TextsrcValidator
    from ._text import TextValidator
    from ._stream import StreamValidator
    from ._spanmode import SpanmodeValidator
    from ._span import SpanValidator
    from ._side import SideValidator
    from ._showlegend import ShowlegendValidator
    from ._selectedpoints import SelectedpointsValidator
    from ._selected import SelectedValidator
    from ._scalemode import ScalemodeValidator
    from ._scalegroup import ScalegroupValidator
    from ._points import PointsValidator
    from ._pointpos import PointposValidator
    from ._orientation import OrientationValidator
    from ._opacity import OpacityValidator
    from ._offsetgroup import OffsetgroupValidator
    from ._name import NameValidator
    from ._metasrc import MetasrcValidator
    from ._meta import MetaValidator
    from ._meanline import MeanlineValidator
    from ._marker import MarkerValidator
    from ._line import LineValidator
    from ._legendgroup import LegendgroupValidator
    from ._jitter import JitterValidator
    from ._idssrc import IdssrcValidator
    from ._ids import IdsValidator
    from ._hovertextsrc import HovertextsrcValidator
    from ._hovertext import HovertextValidator
    from ._hovertemplatesrc import HovertemplatesrcValidator
    from ._hovertemplate import HovertemplateValidator
    from ._hoveron import HoveronValidator
    from ._hoverlabel import HoverlabelValidator
    from ._hoverinfosrc import HoverinfosrcValidator
    from ._hoverinfo import HoverinfoValidator
    from ._fillcolor import FillcolorValidator
    from ._customdatasrc import CustomdatasrcValidator
    from ._customdata import CustomdataValidator
    from ._box import BoxValidator
    from ._bandwidth import BandwidthValidator
    from ._alignmentgroup import AlignmentgroupValidator
else:
    from _plotly_utils.importers import relative_import

    __all__, __getattr__, __dir__ = relative_import(
        __name__,
        [],
        [
            "._ysrc.YsrcValidator",
            "._yaxis.YaxisValidator",
            "._y0.Y0Validator",
            "._y.YValidator",
            "._xsrc.XsrcValidator",
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
            "._legendgroup.LegendgroupValidator",
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
