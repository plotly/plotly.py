import sys

if sys.version_info < (3, 7):
    from ._projection import Projection
    from ._lonaxis import Lonaxis
    from ._lataxis import Lataxis
    from ._domain import Domain
    from ._center import Center
    from . import projection
else:
    from _plotly_utils.importers import relative_import

    __all__, __getattr__ = relative_import(
        __name__,
        [".projection"],
        [
            "._projection.Projection",
            "._lonaxis.Lonaxis",
            "._lataxis.Lataxis",
            "._domain.Domain",
            "._center.Center",
        ],
    )
