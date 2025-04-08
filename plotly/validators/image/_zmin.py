#                   --- THIS FILE IS AUTO-GENERATED ---
# Modifications will be overwitten the next time code generation run.

import _plotly_utils.basevalidators as _bv


class ZminValidator(_bv.InfoArrayValidator):
    def __init__(self, plotly_name="zmin", parent_name="image", **kwargs):
        super().__init__(
            plotly_name,
            parent_name,
            edit_type=kwargs.pop("edit_type", "calc"),
            items=kwargs.pop(
                "items",
                [
                    {"editType": "calc", "valType": "number"},
                    {"editType": "calc", "valType": "number"},
                    {"editType": "calc", "valType": "number"},
                    {"editType": "calc", "valType": "number"},
                ],
            ),
            **kwargs,
        )
