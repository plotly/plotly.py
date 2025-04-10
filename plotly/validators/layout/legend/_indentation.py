#                   --- THIS FILE IS AUTO-GENERATED ---
# Modifications will be overwitten the next time code generation run.

import _plotly_utils.basevalidators as _bv


class IndentationValidator(_bv.NumberValidator):
    def __init__(
        self, plotly_name="indentation", parent_name="layout.legend", **kwargs
    ):
        super().__init__(
            plotly_name,
            parent_name,
            edit_type=kwargs.pop("edit_type", "legend"),
            min=kwargs.pop("min", -15),
            **kwargs,
        )
