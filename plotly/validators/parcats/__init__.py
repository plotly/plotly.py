import sys
from _plotly_utils.importers import relative_import

__all__, __getattr__, __dir__ = relative_import(
    __name__,
    [],
    [
        "._visible.VisibleValidator",
        "._uirevision.UirevisionValidator",
        "._uid.UidValidator",
        "._tickfont.TickfontValidator",
        "._stream.StreamValidator",
        "._sortpaths.SortpathsValidator",
        "._name.NameValidator",
        "._metasrc.MetasrcValidator",
        "._meta.MetaValidator",
        "._line.LineValidator",
        "._legendwidth.LegendwidthValidator",
        "._legendgrouptitle.LegendgrouptitleValidator",
        "._labelfont.LabelfontValidator",
        "._hovertemplate.HovertemplateValidator",
        "._hoveron.HoveronValidator",
        "._hoverinfo.HoverinfoValidator",
        "._domain.DomainValidator",
        "._dimensiondefaults.DimensiondefaultsValidator",
        "._dimensions.DimensionsValidator",
        "._countssrc.CountssrcValidator",
        "._counts.CountsValidator",
        "._bundlecolors.BundlecolorsValidator",
        "._arrangement.ArrangementValidator",
    ],
)
