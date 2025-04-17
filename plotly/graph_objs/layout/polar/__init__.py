import sys
from _plotly_utils.importers import relative_import

__all__, __getattr__, __dir__ = relative_import(
    __name__,
    [".angularaxis", ".radialaxis"],
    ["._angularaxis.AngularAxis", "._domain.Domain", "._radialaxis.RadialAxis"],
)
