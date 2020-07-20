import sys

if sys.version_info < (3, 7):
    from ._aaxis import Aaxis
    from ._baxis import Baxis
    from ._font import Font
    from ._stream import Stream
    from . import aaxis
    from . import baxis
else:
    from _plotly_utils.importers import relative_import

    __all__, __getattr__, __dir__ = relative_import(
        __name__,
        [".aaxis", ".baxis"],
        ["._aaxis.Aaxis", "._baxis.Baxis", "._font.Font", "._stream.Stream"],
    )
