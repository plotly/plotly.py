#                   --- THIS FILE IS AUTO-GENERATED ---
# Modifications will be overwitten the next time code generation run.

import _plotly_utils.basevalidators as _bv


class RangemodeValidator(_bv.EnumeratedValidator):
    def __init__(
        self,
        plotly_name="rangemode",
        parent_name="layout.xaxis.rangeslider.yaxis",
        **kwargs,
    ):
        super().__init__(
            plotly_name,
            parent_name,
            edit_type=kwargs.pop("edit_type", "calc"),
            values=kwargs.pop("values", ["auto", "fixed", "match"]),
            **kwargs,
        )
