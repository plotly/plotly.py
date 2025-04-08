#                   --- THIS FILE IS AUTO-GENERATED ---
# Modifications will be overwitten the next time code generation run.

import _plotly_utils.basevalidators as _bv


class FlipValidator(_bv.FlaglistValidator):
    def __init__(self, plotly_name="flip", parent_name="treemap.tiling", **kwargs):
        super().__init__(
            plotly_name,
            parent_name,
            edit_type=kwargs.pop("edit_type", "plot"),
            flags=kwargs.pop("flags", ["x", "y"]),
            **kwargs,
        )
