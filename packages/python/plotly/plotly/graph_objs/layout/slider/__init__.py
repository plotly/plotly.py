import sys

if sys.version_info < (3, 7):
    from ._transition import Transition
    from ._step import Step
    from ._pad import Pad
    from ._font import Font
    from ._currentvalue import Currentvalue
    from . import currentvalue
else:
    from _plotly_utils.importers import relative_import

    __all__, __getattr__, __dir__ = relative_import(
        __name__,
        [".currentvalue"],
        [
            "._transition.Transition",
            "._step.Step",
            "._pad.Pad",
            "._font.Font",
            "._currentvalue.Currentvalue",
        ],
    )
