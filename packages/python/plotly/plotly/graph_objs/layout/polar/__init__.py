import sys

if sys.version_info < (3, 7):
    from ._radialaxis import RadialAxis
    from ._domain import Domain
    from ._angularaxis import AngularAxis
    from . import radialaxis
    from . import angularaxis
else:
    from _plotly_utils.importers import relative_import

    __all__, __getattr__ = relative_import(
        __name__,
        [".radialaxis", ".angularaxis"],
        ["._radialaxis.RadialAxis", "._domain.Domain", "._angularaxis.AngularAxis"],
    )
