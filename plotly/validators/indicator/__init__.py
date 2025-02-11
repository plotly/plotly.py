import sys
from _plotly_utils.importers import relative_import

__all__, __getattr__, __dir__ = relative_import(
    __name__,
    [],
    [
        "._visible.VisibleValidator",
        "._value.ValueValidator",
        "._uirevision.UirevisionValidator",
        "._uid.UidValidator",
        "._title.TitleValidator",
        "._stream.StreamValidator",
        "._number.NumberValidator",
        "._name.NameValidator",
        "._mode.ModeValidator",
        "._metasrc.MetasrcValidator",
        "._meta.MetaValidator",
        "._legendwidth.LegendwidthValidator",
        "._legendrank.LegendrankValidator",
        "._legendgrouptitle.LegendgrouptitleValidator",
        "._legend.LegendValidator",
        "._idssrc.IdssrcValidator",
        "._ids.IdsValidator",
        "._gauge.GaugeValidator",
        "._domain.DomainValidator",
        "._delta.DeltaValidator",
        "._customdatasrc.CustomdatasrcValidator",
        "._customdata.CustomdataValidator",
        "._align.AlignValidator",
    ],
)
