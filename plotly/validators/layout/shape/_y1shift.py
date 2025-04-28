#                   --- THIS FILE IS AUTO-GENERATED ---
# Modifications will be overwitten the next time code generation run.

import _plotly_utils.basevalidators as _bv


class Y1ShiftValidator(_bv.NumberValidator):
    def __init__(self, plotly_name="y1shift", parent_name="layout.shape", **kwargs):
        super().__init__(
            plotly_name,
            parent_name,
            edit_type=kwargs.pop("edit_type", "calc"),
            max=kwargs.pop("max", 1),
            min=kwargs.pop("min", -1),
            **kwargs,
        )
