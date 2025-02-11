import sys
from _plotly_utils.importers import relative_import

__all__, __getattr__, __dir__ = relative_import(
    __name__,
    [],
    [
        "._ysrc.YsrcValidator",
        "._y.YValidator",
        "._xsrc.XsrcValidator",
        "._x.XValidator",
        "._thickness.ThicknessValidator",
        "._pad.PadValidator",
        "._line.LineValidator",
        "._labelsrc.LabelsrcValidator",
        "._label.LabelValidator",
        "._hovertemplatesrc.HovertemplatesrcValidator",
        "._hovertemplate.HovertemplateValidator",
        "._hoverlabel.HoverlabelValidator",
        "._hoverinfo.HoverinfoValidator",
        "._groups.GroupsValidator",
        "._customdatasrc.CustomdatasrcValidator",
        "._customdata.CustomdataValidator",
        "._colorsrc.ColorsrcValidator",
        "._color.ColorValidator",
        "._align.AlignValidator",
    ],
)
