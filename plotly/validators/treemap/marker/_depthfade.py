#                   --- THIS FILE IS AUTO-GENERATED ---
# Modifications will be overwitten the next time code generation run.

import _plotly_utils.basevalidators as _bv


class DepthfadeValidator(_bv.EnumeratedValidator):
    def __init__(self, plotly_name="depthfade", parent_name="treemap.marker", **kwargs):
        super().__init__(
            plotly_name,
            parent_name,
            edit_type=kwargs.pop("edit_type", "style"),
            values=kwargs.pop("values", [True, False, "reversed"]),
            **kwargs,
        )
