import sys

if sys.version_info < (3, 7):
    from ._title import Title
    from ._tickformatstop import Tickformatstop
    from ._tickfont import Tickfont
    from ._rangeslider import Rangeslider
    from ._rangeselector import Rangeselector
    from ._rangebreak import Rangebreak
    from . import title
    from . import rangeslider
    from . import rangeselector
else:
    from _plotly_utils.importers import relative_import

    __all__, __getattr__, __dir__ = relative_import(
        __name__,
        [".title", ".rangeslider", ".rangeselector"],
        [
            "._title.Title",
            "._tickformatstop.Tickformatstop",
            "._tickfont.Tickfont",
            "._rangeslider.Rangeslider",
            "._rangeselector.Rangeselector",
            "._rangebreak.Rangebreak",
        ],
    )
