#                   --- THIS FILE IS AUTO-GENERATED ---
# Modifications will be overwitten the next time code generation run.

import _plotly_utils.basevalidators as _bv


class ColorValidator(_bv.ColorValidator):
    def __init__(
        self, plotly_name="color", parent_name="scatterternary.marker.line", **kwargs
    ):
        super().__init__(
            plotly_name,
            parent_name,
            array_ok=kwargs.pop("array_ok", True),
            edit_type=kwargs.pop("edit_type", "style"),
            colorscale_path=kwargs.pop(
                "colorscale_path", "scatterternary.marker.line.colorscale"
            ),
            **kwargs,
        )
