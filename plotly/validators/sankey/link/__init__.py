import sys
from _plotly_utils.importers import relative_import

__all__, __getattr__, __dir__ = relative_import(
    __name__,
    [],
    [
        "._valuesrc.ValuesrcValidator",
        "._value.ValueValidator",
        "._targetsrc.TargetsrcValidator",
        "._target.TargetValidator",
        "._sourcesrc.SourcesrcValidator",
        "._source.SourceValidator",
        "._line.LineValidator",
        "._labelsrc.LabelsrcValidator",
        "._label.LabelValidator",
        "._hovertemplatesrc.HovertemplatesrcValidator",
        "._hovertemplate.HovertemplateValidator",
        "._hoverlabel.HoverlabelValidator",
        "._hoverinfo.HoverinfoValidator",
        "._hovercolorsrc.HovercolorsrcValidator",
        "._hovercolor.HovercolorValidator",
        "._customdatasrc.CustomdatasrcValidator",
        "._customdata.CustomdataValidator",
        "._colorsrc.ColorsrcValidator",
        "._colorscaledefaults.ColorscaledefaultsValidator",
        "._colorscales.ColorscalesValidator",
        "._color.ColorValidator",
        "._arrowlen.ArrowlenValidator",
    ],
)
