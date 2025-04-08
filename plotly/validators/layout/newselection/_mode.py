#                   --- THIS FILE IS AUTO-GENERATED ---
# Modifications will be overwitten the next time code generation run.

import _plotly_utils.basevalidators as _bv


class ModeValidator(_bv.EnumeratedValidator):
    def __init__(self, plotly_name="mode", parent_name="layout.newselection", **kwargs):
        super().__init__(
            plotly_name,
            parent_name,
            edit_type=kwargs.pop("edit_type", "none"),
            values=kwargs.pop("values", ["immediate", "gradual"]),
            **kwargs,
        )
