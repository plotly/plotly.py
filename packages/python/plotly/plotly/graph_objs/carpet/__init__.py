import sys

if sys.version_info < (3, 7):
    from ._stream import Stream
    from ._font import Font
    from ._baxis import Baxis
    from ._aaxis import Aaxis
    from . import baxis
    from . import aaxis
else:
    from _plotly_utils.importers import relative_import

    __all__, __getattr__ = relative_import(
        __name__,
        [".baxis", ".aaxis"],
        ["._stream.Stream", "._font.Font", "._baxis.Baxis", "._aaxis.Aaxis"],
    )
