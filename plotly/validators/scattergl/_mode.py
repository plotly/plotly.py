#                   --- THIS FILE IS AUTO-GENERATED ---
# Modifications will be overwitten the next time code generation run.

import _plotly_utils.basevalidators as _bv


class ModeValidator(_bv.FlaglistValidator):
    def __init__(self, plotly_name="mode", parent_name="scattergl", **kwargs):
        super().__init__(
            plotly_name,
            parent_name,
            edit_type=kwargs.pop("edit_type", "calc"),
            extras=kwargs.pop("extras", ["none"]),
            flags=kwargs.pop("flags", ["lines", "markers", "text"]),
            **kwargs,
        )
