import sys

if sys.version_info < (3, 7):
    from ._angularaxis import AngularAxis
    from ._domain import Domain
    from ._radialaxis import RadialAxis
    from . import angularaxis
    from . import radialaxis
else:
    from _plotly_utils.importers import relative_import

    __all__, __getattr__, __dir__ = relative_import(
        __name__,
        [".angularaxis", ".radialaxis"],
        ["._angularaxis.AngularAxis", "._domain.Domain", "._radialaxis.RadialAxis"],
    )
