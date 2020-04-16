import sys

if sys.version_info < (3, 7):
    from ._domain import Domain
    from ._caxis import Caxis
    from ._baxis import Baxis
    from ._aaxis import Aaxis
    from . import caxis
    from . import baxis
    from . import aaxis
else:
    from _plotly_utils.importers import relative_import

    __all__, __getattr__, __dir__ = relative_import(
        __name__,
        [".caxis", ".baxis", ".aaxis"],
        ["._domain.Domain", "._caxis.Caxis", "._baxis.Baxis", "._aaxis.Aaxis"],
    )
