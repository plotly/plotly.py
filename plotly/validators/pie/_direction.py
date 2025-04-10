#                   --- THIS FILE IS AUTO-GENERATED ---
# Modifications will be overwitten the next time code generation run.

import _plotly_utils.basevalidators as _bv


class DirectionValidator(_bv.EnumeratedValidator):
    def __init__(self, plotly_name="direction", parent_name="pie", **kwargs):
        super().__init__(
            plotly_name,
            parent_name,
            edit_type=kwargs.pop("edit_type", "calc"),
            values=kwargs.pop("values", ["clockwise", "counterclockwise"]),
            **kwargs,
        )
