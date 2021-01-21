import sys

if sys.version_info < (3, 7):
    from ._tickfont import Tickfont
    from ._tickformatstops import Tickformatstops
else:
    from _plotly_utils.importers import relative_import

    __all__, __getattr__, __dir__ = relative_import(
        __name__, [], ["._tickfont.Tickfont", "._tickformatstops.Tickformatstops"]
    )
