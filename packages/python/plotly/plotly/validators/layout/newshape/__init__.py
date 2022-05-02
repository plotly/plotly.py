import sys
from typing import TYPE_CHECKING

if sys.version_info < (3, 7) or TYPE_CHECKING:
    from ._opacity import OpacityValidator
    from ._line import LineValidator
    from ._layer import LayerValidator
    from ._fillrule import FillruleValidator
    from ._fillcolor import FillcolorValidator
    from ._drawdirection import DrawdirectionValidator
else:
    from _plotly_utils.importers import relative_import

    __all__, __getattr__, __dir__ = relative_import(
        __name__,
        [],
        [
            "._opacity.OpacityValidator",
            "._line.LineValidator",
            "._layer.LayerValidator",
            "._fillrule.FillruleValidator",
            "._fillcolor.FillcolorValidator",
            "._drawdirection.DrawdirectionValidator",
        ],
    )
