import sys

if sys.version_info < (3, 7):
    from ._rangebreak import Rangebreak
    from ._rangeselector import Rangeselector
    from ._rangeslider import Rangeslider
    from ._tickfont import Tickfont
    from ._tickformatstop import Tickformatstop
    from ._title import Title
    from . import rangeselector
    from . import rangeslider
    from . import title
else:
    from _plotly_utils.importers import relative_import

    __all__, __getattr__, __dir__ = relative_import(
        __name__,
        [".rangeselector", ".rangeslider", ".title"],
        [
            "._rangebreak.Rangebreak",
            "._rangeselector.Rangeselector",
            "._rangeslider.Rangeslider",
            "._tickfont.Tickfont",
            "._tickformatstop.Tickformatstop",
            "._title.Title",
        ],
    )
