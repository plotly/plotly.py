#                   --- THIS FILE IS AUTO-GENERATED ---
# Modifications will be overwitten the next time code generation run.

import _plotly_utils.basevalidators as _bv


class ValuesValidator(_bv.InfoArrayValidator):
    def __init__(
        self, plotly_name="values", parent_name="layout.yaxis.rangebreak", **kwargs
    ):
        super().__init__(
            plotly_name,
            parent_name,
            edit_type=kwargs.pop("edit_type", "calc"),
            free_length=kwargs.pop("free_length", True),
            items=kwargs.pop("items", {"editType": "calc", "valType": "any"}),
            **kwargs,
        )
