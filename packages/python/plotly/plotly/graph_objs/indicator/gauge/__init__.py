import sys

if sys.version_info < (3, 7):
    from ._threshold import Threshold
    from ._step import Step
    from ._bar import Bar
    from ._axis import Axis
    from . import threshold
    from . import step
    from . import bar
    from . import axis
else:
    from _plotly_utils.importers import relative_import

    __all__, __getattr__ = relative_import(
        __name__,
        [".threshold", ".step", ".bar", ".axis"],
        ["._threshold.Threshold", "._step.Step", "._bar.Bar", "._axis.Axis"],
    )
