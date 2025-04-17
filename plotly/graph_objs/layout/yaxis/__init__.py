import sys
from _plotly_utils.importers import relative_import

__all__, __getattr__, __dir__ = relative_import(
    __name__,
    [".title"],
    [
        "._autorangeoptions.Autorangeoptions",
        "._minor.Minor",
        "._rangebreak.Rangebreak",
        "._tickfont.Tickfont",
        "._tickformatstop.Tickformatstop",
        "._title.Title",
    ],
)
