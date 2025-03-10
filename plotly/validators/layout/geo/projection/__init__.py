import sys
from _plotly_utils.importers import relative_import

__all__, __getattr__, __dir__ = relative_import(
    __name__,
    [],
    [
        "._type.TypeValidator",
        "._tilt.TiltValidator",
        "._scale.ScaleValidator",
        "._rotation.RotationValidator",
        "._parallels.ParallelsValidator",
        "._distance.DistanceValidator",
    ],
)
