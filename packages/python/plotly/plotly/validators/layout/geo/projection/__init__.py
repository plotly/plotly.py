import sys

if sys.version_info < (3, 7):
    from ._type import TypeValidator
    from ._scale import ScaleValidator
    from ._rotation import RotationValidator
    from ._parallels import ParallelsValidator
else:
    from _plotly_utils.importers import relative_import

    __all__, __getattr__, __dir__ = relative_import(
        __name__,
        [],
        [
            "._type.TypeValidator",
            "._scale.ScaleValidator",
            "._rotation.RotationValidator",
            "._parallels.ParallelsValidator",
        ],
    )
