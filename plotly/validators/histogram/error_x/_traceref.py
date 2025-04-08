#                   --- THIS FILE IS AUTO-GENERATED ---
# Modifications will be overwitten the next time code generation run.

import _plotly_utils.basevalidators as _bv


class TracerefValidator(_bv.IntegerValidator):
    def __init__(
        self, plotly_name="traceref", parent_name="histogram.error_x", **kwargs
    ):
        super().__init__(
            plotly_name,
            parent_name,
            edit_type=kwargs.pop("edit_type", "style"),
            min=kwargs.pop("min", 0),
            **kwargs,
        )
