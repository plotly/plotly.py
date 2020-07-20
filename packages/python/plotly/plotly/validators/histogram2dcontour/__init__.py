import sys

if sys.version_info < (3, 7):
    from ._zsrc import ZsrcValidator
    from ._zmin import ZminValidator
    from ._zmid import ZmidValidator
    from ._zmax import ZmaxValidator
    from ._zhoverformat import ZhoverformatValidator
    from ._zauto import ZautoValidator
    from ._z import ZValidator
    from ._ysrc import YsrcValidator
    from ._ycalendar import YcalendarValidator
    from ._ybins import YbinsValidator
    from ._ybingroup import YbingroupValidator
    from ._yaxis import YaxisValidator
    from ._y import YValidator
    from ._xsrc import XsrcValidator
    from ._xcalendar import XcalendarValidator
    from ._xbins import XbinsValidator
    from ._xbingroup import XbingroupValidator
    from ._xaxis import XaxisValidator
    from ._x import XValidator
    from ._visible import VisibleValidator
    from ._uirevision import UirevisionValidator
    from ._uid import UidValidator
    from ._stream import StreamValidator
    from ._showscale import ShowscaleValidator
    from ._showlegend import ShowlegendValidator
    from ._reversescale import ReversescaleValidator
    from ._opacity import OpacityValidator
    from ._ncontours import NcontoursValidator
    from ._nbinsy import NbinsyValidator
    from ._nbinsx import NbinsxValidator
    from ._name import NameValidator
    from ._metasrc import MetasrcValidator
    from ._meta import MetaValidator
    from ._marker import MarkerValidator
    from ._line import LineValidator
    from ._legendgroup import LegendgroupValidator
    from ._idssrc import IdssrcValidator
    from ._ids import IdsValidator
    from ._hovertemplatesrc import HovertemplatesrcValidator
    from ._hovertemplate import HovertemplateValidator
    from ._hoverlabel import HoverlabelValidator
    from ._hoverinfosrc import HoverinfosrcValidator
    from ._hoverinfo import HoverinfoValidator
    from ._histnorm import HistnormValidator
    from ._histfunc import HistfuncValidator
    from ._customdatasrc import CustomdatasrcValidator
    from ._customdata import CustomdataValidator
    from ._contours import ContoursValidator
    from ._colorscale import ColorscaleValidator
    from ._colorbar import ColorbarValidator
    from ._coloraxis import ColoraxisValidator
    from ._bingroup import BingroupValidator
    from ._autocontour import AutocontourValidator
    from ._autocolorscale import AutocolorscaleValidator
    from ._autobiny import AutobinyValidator
    from ._autobinx import AutobinxValidator
else:
    from _plotly_utils.importers import relative_import

    __all__, __getattr__, __dir__ = relative_import(
        __name__,
        [],
        [
            "._zsrc.ZsrcValidator",
            "._zmin.ZminValidator",
            "._zmid.ZmidValidator",
            "._zmax.ZmaxValidator",
            "._zhoverformat.ZhoverformatValidator",
            "._zauto.ZautoValidator",
            "._z.ZValidator",
            "._ysrc.YsrcValidator",
            "._ycalendar.YcalendarValidator",
            "._ybins.YbinsValidator",
            "._ybingroup.YbingroupValidator",
            "._yaxis.YaxisValidator",
            "._y.YValidator",
            "._xsrc.XsrcValidator",
            "._xcalendar.XcalendarValidator",
            "._xbins.XbinsValidator",
            "._xbingroup.XbingroupValidator",
            "._xaxis.XaxisValidator",
            "._x.XValidator",
            "._visible.VisibleValidator",
            "._uirevision.UirevisionValidator",
            "._uid.UidValidator",
            "._stream.StreamValidator",
            "._showscale.ShowscaleValidator",
            "._showlegend.ShowlegendValidator",
            "._reversescale.ReversescaleValidator",
            "._opacity.OpacityValidator",
            "._ncontours.NcontoursValidator",
            "._nbinsy.NbinsyValidator",
            "._nbinsx.NbinsxValidator",
            "._name.NameValidator",
            "._metasrc.MetasrcValidator",
            "._meta.MetaValidator",
            "._marker.MarkerValidator",
            "._line.LineValidator",
            "._legendgroup.LegendgroupValidator",
            "._idssrc.IdssrcValidator",
            "._ids.IdsValidator",
            "._hovertemplatesrc.HovertemplatesrcValidator",
            "._hovertemplate.HovertemplateValidator",
            "._hoverlabel.HoverlabelValidator",
            "._hoverinfosrc.HoverinfosrcValidator",
            "._hoverinfo.HoverinfoValidator",
            "._histnorm.HistnormValidator",
            "._histfunc.HistfuncValidator",
            "._customdatasrc.CustomdatasrcValidator",
            "._customdata.CustomdataValidator",
            "._contours.ContoursValidator",
            "._colorscale.ColorscaleValidator",
            "._colorbar.ColorbarValidator",
            "._coloraxis.ColoraxisValidator",
            "._bingroup.BingroupValidator",
            "._autocontour.AutocontourValidator",
            "._autocolorscale.AutocolorscaleValidator",
            "._autobiny.AutobinyValidator",
            "._autobinx.AutobinxValidator",
        ],
    )
