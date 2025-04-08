#                   --- THIS FILE IS AUTO-GENERATED ---
# Modifications will be overwitten the next time code generation run.

import _plotly_utils.basevalidators as _bv


class SizeValidator(_bv.NumberValidator):
    def __init__(
        self,
        plotly_name="size",
        parent_name="layout.annotation.hoverlabel.font",
        **kwargs,
    ):
        super().__init__(
            plotly_name,
            parent_name,
            edit_type=kwargs.pop("edit_type", "arraydraw"),
            min=kwargs.pop("min", 1),
            **kwargs,
        )
