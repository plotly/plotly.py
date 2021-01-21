import sys

if sys.version_info < (3, 7):
    from ._axis import Axis
    from ._bar import Bar
    from ._steps import Steps
    from ._threshold import Threshold
    from . import axis
    from . import bar
    from . import threshold
else:
    from _plotly_utils.importers import relative_import

    __all__, __getattr__, __dir__ = relative_import(
        __name__,
        [".axis", ".bar", ".threshold"],
        ["._axis.Axis", "._bar.Bar", "._steps.Steps", "._threshold.Threshold"],
    )
