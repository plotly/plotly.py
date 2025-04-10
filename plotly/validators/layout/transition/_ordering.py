#                   --- THIS FILE IS AUTO-GENERATED ---
# Modifications will be overwitten the next time code generation run.

import _plotly_utils.basevalidators as _bv


class OrderingValidator(_bv.EnumeratedValidator):
    def __init__(
        self, plotly_name="ordering", parent_name="layout.transition", **kwargs
    ):
        super().__init__(
            plotly_name,
            parent_name,
            edit_type=kwargs.pop("edit_type", "none"),
            values=kwargs.pop("values", ["layout first", "traces first"]),
            **kwargs,
        )
