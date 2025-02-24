import sys
from _plotly_utils.importers import relative_import

__all__, __getattr__, __dir__ = relative_import(
    __name__,
    [".rangeselector", ".rangeslider", ".title"],
    [
        "._autorangeoptions.Autorangeoptions",
        "._minor.Minor",
        "._rangebreak.Rangebreak",
        "._rangeselector.Rangeselector",
        "._rangeslider.Rangeslider",
        "._tickfont.Tickfont",
        "._tickformatstop.Tickformatstop",
        "._title.Title",
    ],
)
