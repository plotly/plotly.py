#                   --- THIS FILE IS AUTO-GENERATED ---
# Modifications will be overwitten the next time code generation run.

import _plotly_utils.basevalidators as _bv


class DashValidator(_bv.DashValidator):
    def __init__(
        self, plotly_name="dash", parent_name="layout.selection.line", **kwargs
    ):
        super().__init__(
            plotly_name,
            parent_name,
            edit_type=kwargs.pop("edit_type", "arraydraw"),
            values=kwargs.pop(
                "values", ["solid", "dot", "dash", "longdash", "dashdot", "longdashdot"]
            ),
            **kwargs,
        )
