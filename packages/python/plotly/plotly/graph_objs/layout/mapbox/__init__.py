import sys

if sys.version_info < (3, 7):
    from ._layer import Layer
    from ._domain import Domain
    from ._center import Center
    from . import layer
else:
    from _plotly_utils.importers import relative_import

    __all__, __getattr__ = relative_import(
        __name__, [".layer"], ["._layer.Layer", "._domain.Domain", "._center.Center"]
    )
