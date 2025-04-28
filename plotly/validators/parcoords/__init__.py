import sys
from _plotly_utils.importers import relative_import

__all__, __getattr__, __dir__ = relative_import(
    __name__,
    [],
    [
        "._visible.VisibleValidator",
        "._unselected.UnselectedValidator",
        "._uirevision.UirevisionValidator",
        "._uid.UidValidator",
        "._tickfont.TickfontValidator",
        "._stream.StreamValidator",
        "._rangefont.RangefontValidator",
        "._name.NameValidator",
        "._metasrc.MetasrcValidator",
        "._meta.MetaValidator",
        "._line.LineValidator",
        "._legendwidth.LegendwidthValidator",
        "._legendrank.LegendrankValidator",
        "._legendgrouptitle.LegendgrouptitleValidator",
        "._legend.LegendValidator",
        "._labelside.LabelsideValidator",
        "._labelfont.LabelfontValidator",
        "._labelangle.LabelangleValidator",
        "._idssrc.IdssrcValidator",
        "._ids.IdsValidator",
        "._domain.DomainValidator",
        "._dimensiondefaults.DimensiondefaultsValidator",
        "._dimensions.DimensionsValidator",
        "._customdatasrc.CustomdatasrcValidator",
        "._customdata.CustomdataValidator",
    ],
)
