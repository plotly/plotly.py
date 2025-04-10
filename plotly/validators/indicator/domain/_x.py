#                   --- THIS FILE IS AUTO-GENERATED ---
# Modifications will be overwitten the next time code generation run.

import _plotly_utils.basevalidators as _bv


class XValidator(_bv.InfoArrayValidator):
    def __init__(self, plotly_name="x", parent_name="indicator.domain", **kwargs):
        super().__init__(
            plotly_name,
            parent_name,
            edit_type=kwargs.pop("edit_type", "calc"),
            items=kwargs.pop(
                "items",
                [
                    {"editType": "calc", "max": 1, "min": 0, "valType": "number"},
                    {"editType": "calc", "max": 1, "min": 0, "valType": "number"},
                ],
            ),
            **kwargs,
        )
