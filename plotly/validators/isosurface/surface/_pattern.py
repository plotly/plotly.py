#                   --- THIS FILE IS AUTO-GENERATED ---
# Modifications will be overwitten the next time code generation run.

import _plotly_utils.basevalidators as _bv


class PatternValidator(_bv.FlaglistValidator):
    def __init__(
        self, plotly_name="pattern", parent_name="isosurface.surface", **kwargs
    ):
        super().__init__(
            plotly_name,
            parent_name,
            edit_type=kwargs.pop("edit_type", "calc"),
            extras=kwargs.pop("extras", ["all", "odd", "even"]),
            flags=kwargs.pop("flags", ["A", "B", "C", "D", "E"]),
            **kwargs,
        )
