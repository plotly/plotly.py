import sys

if sys.version_info < (3, 7):
    from ._up import Up
    from ._projection import Projection
    from ._eye import Eye
    from ._center import Center
else:
    from _plotly_utils.importers import relative_import

    __all__, __getattr__ = relative_import(
        __name__,
        [],
        ["._up.Up", "._projection.Projection", "._eye.Eye", "._center.Center"],
    )
