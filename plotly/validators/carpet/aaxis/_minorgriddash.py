#                   --- THIS FILE IS AUTO-GENERATED ---
# Modifications will be overwitten the next time code generation run.

import _plotly_utils.basevalidators as _bv


class MinorgriddashValidator(_bv.DashValidator):
    def __init__(
        self, plotly_name="minorgriddash", parent_name="carpet.aaxis", **kwargs
    ):
        super().__init__(
            plotly_name,
            parent_name,
            edit_type=kwargs.pop("edit_type", "calc"),
            values=kwargs.pop(
                "values", ["solid", "dot", "dash", "longdash", "dashdot", "longdashdot"]
            ),
            **kwargs,
        )
