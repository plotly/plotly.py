#                   --- THIS FILE IS AUTO-GENERATED ---
# Modifications will be overwitten the next time code generation run.

import _plotly_utils.basevalidators as _bv


class TickmodeValidator(_bv.EnumeratedValidator):
    def __init__(
        self, plotly_name="tickmode", parent_name="surface.colorbar", **kwargs
    ):
        super().__init__(
            plotly_name,
            parent_name,
            edit_type=kwargs.pop("edit_type", "calc"),
            implied_edits=kwargs.pop("implied_edits", {}),
            values=kwargs.pop("values", ["auto", "linear", "array"]),
            **kwargs,
        )
