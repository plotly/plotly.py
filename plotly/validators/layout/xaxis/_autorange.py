#                   --- THIS FILE IS AUTO-GENERATED ---
# Modifications will be overwitten the next time code generation run.

import _plotly_utils.basevalidators as _bv


class AutorangeValidator(_bv.EnumeratedValidator):
    def __init__(self, plotly_name="autorange", parent_name="layout.xaxis", **kwargs):
        super().__init__(
            plotly_name,
            parent_name,
            edit_type=kwargs.pop("edit_type", "axrange"),
            implied_edits=kwargs.pop("implied_edits", {}),
            values=kwargs.pop(
                "values",
                [True, False, "reversed", "min reversed", "max reversed", "min", "max"],
            ),
            **kwargs,
        )
