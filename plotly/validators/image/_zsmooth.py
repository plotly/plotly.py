#                   --- THIS FILE IS AUTO-GENERATED ---
# Modifications will be overwitten the next time code generation run.

import _plotly_utils.basevalidators as _bv


class ZsmoothValidator(_bv.EnumeratedValidator):
    def __init__(self, plotly_name="zsmooth", parent_name="image", **kwargs):
        super().__init__(
            plotly_name,
            parent_name,
            edit_type=kwargs.pop("edit_type", "plot"),
            values=kwargs.pop("values", ["fast", False]),
            **kwargs,
        )
