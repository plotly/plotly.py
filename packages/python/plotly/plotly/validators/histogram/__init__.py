import sys

if sys.version_info < (3, 7):
    from ._ysrc import YsrcValidator
    from ._ycalendar import YcalendarValidator
    from ._ybins import YbinsValidator
    from ._yaxis import YaxisValidator
    from ._y import YValidator
    from ._xsrc import XsrcValidator
    from ._xcalendar import XcalendarValidator
    from ._xbins import XbinsValidator
    from ._xaxis import XaxisValidator
    from ._x import XValidator
    from ._visible import VisibleValidator
    from ._unselected import UnselectedValidator
    from ._uirevision import UirevisionValidator
    from ._uid import UidValidator
    from ._textsrc import TextsrcValidator
    from ._text import TextValidator
    from ._stream import StreamValidator
    from ._showlegend import ShowlegendValidator
    from ._selectedpoints import SelectedpointsValidator
    from ._selected import SelectedValidator
    from ._orientation import OrientationValidator
    from ._opacity import OpacityValidator
    from ._offsetgroup import OffsetgroupValidator
    from ._nbinsy import NbinsyValidator
    from ._nbinsx import NbinsxValidator
    from ._name import NameValidator
    from ._metasrc import MetasrcValidator
    from ._meta import MetaValidator
    from ._marker import MarkerValidator
    from ._legendgroup import LegendgroupValidator
    from ._idssrc import IdssrcValidator
    from ._ids import IdsValidator
    from ._hovertextsrc import HovertextsrcValidator
    from ._hovertext import HovertextValidator
    from ._hovertemplatesrc import HovertemplatesrcValidator
    from ._hovertemplate import HovertemplateValidator
    from ._hoverlabel import HoverlabelValidator
    from ._hoverinfosrc import HoverinfosrcValidator
    from ._hoverinfo import HoverinfoValidator
    from ._histnorm import HistnormValidator
    from ._histfunc import HistfuncValidator
    from ._error_y import Error_YValidator
    from ._error_x import Error_XValidator
    from ._customdatasrc import CustomdatasrcValidator
    from ._customdata import CustomdataValidator
    from ._cumulative import CumulativeValidator
    from ._bingroup import BingroupValidator
    from ._autobiny import AutobinyValidator
    from ._autobinx import AutobinxValidator
    from ._alignmentgroup import AlignmentgroupValidator
else:
    from _plotly_utils.importers import relative_import

    __all__, __getattr__, __dir__ = relative_import(
        __name__,
        [],
        [
            "._ysrc.YsrcValidator",
            "._ycalendar.YcalendarValidator",
            "._ybins.YbinsValidator",
            "._yaxis.YaxisValidator",
            "._y.YValidator",
            "._xsrc.XsrcValidator",
            "._xcalendar.XcalendarValidator",
            "._xbins.XbinsValidator",
            "._xaxis.XaxisValidator",
            "._x.XValidator",
            "._visible.VisibleValidator",
            "._unselected.UnselectedValidator",
            "._uirevision.UirevisionValidator",
            "._uid.UidValidator",
            "._textsrc.TextsrcValidator",
            "._text.TextValidator",
            "._stream.StreamValidator",
            "._showlegend.ShowlegendValidator",
            "._selectedpoints.SelectedpointsValidator",
            "._selected.SelectedValidator",
            "._orientation.OrientationValidator",
            "._opacity.OpacityValidator",
            "._offsetgroup.OffsetgroupValidator",
            "._nbinsy.NbinsyValidator",
            "._nbinsx.NbinsxValidator",
            "._name.NameValidator",
            "._metasrc.MetasrcValidator",
            "._meta.MetaValidator",
            "._marker.MarkerValidator",
            "._legendgroup.LegendgroupValidator",
            "._idssrc.IdssrcValidator",
            "._ids.IdsValidator",
            "._hovertextsrc.HovertextsrcValidator",
            "._hovertext.HovertextValidator",
            "._hovertemplatesrc.HovertemplatesrcValidator",
            "._hovertemplate.HovertemplateValidator",
            "._hoverlabel.HoverlabelValidator",
            "._hoverinfosrc.HoverinfosrcValidator",
            "._hoverinfo.HoverinfoValidator",
            "._histnorm.HistnormValidator",
            "._histfunc.HistfuncValidator",
            "._error_y.Error_YValidator",
            "._error_x.Error_XValidator",
            "._customdatasrc.CustomdatasrcValidator",
            "._customdata.CustomdataValidator",
            "._cumulative.CumulativeValidator",
            "._bingroup.BingroupValidator",
            "._autobiny.AutobinyValidator",
            "._autobinx.AutobinxValidator",
            "._alignmentgroup.AlignmentgroupValidator",
        ],
    )
