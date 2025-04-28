#                   --- THIS FILE IS AUTO-GENERATED ---
# Modifications will be overwitten the next time code generation run.

import _plotly_utils.basevalidators as _bv


class ConstraintowardValidator(_bv.EnumeratedValidator):
    def __init__(
        self, plotly_name="constraintoward", parent_name="layout.yaxis", **kwargs
    ):
        super().__init__(
            plotly_name,
            parent_name,
            edit_type=kwargs.pop("edit_type", "plot"),
            values=kwargs.pop(
                "values", ["left", "center", "right", "top", "middle", "bottom"]
            ),
            **kwargs,
        )
