#                   --- THIS FILE IS AUTO-GENERATED ---
# Modifications will be overwitten the next time code generation run.

import _plotly_utils.basevalidators as _bv


class SpanValidator(_bv.InfoArrayValidator):
    def __init__(self, plotly_name="span", parent_name="violin", **kwargs):
        super().__init__(
            plotly_name,
            parent_name,
            edit_type=kwargs.pop("edit_type", "calc"),
            items=kwargs.pop(
                "items",
                [
                    {"editType": "calc", "valType": "any"},
                    {"editType": "calc", "valType": "any"},
                ],
            ),
            **kwargs,
        )
