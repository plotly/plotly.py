#                   --- THIS FILE IS AUTO-GENERATED ---
# Modifications will be overwitten the next time code generation run.

import _plotly_utils.basevalidators as _bv


class MethodValidator(_bv.EnumeratedValidator):
    def __init__(
        self, plotly_name="method", parent_name="layout.updatemenu.button", **kwargs
    ):
        super().__init__(
            plotly_name,
            parent_name,
            edit_type=kwargs.pop("edit_type", "arraydraw"),
            values=kwargs.pop(
                "values", ["restyle", "relayout", "animate", "update", "skip"]
            ),
            **kwargs,
        )
