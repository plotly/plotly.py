#                   --- THIS FILE IS AUTO-GENERATED ---
# Modifications will be overwitten the next time code generation run.

import _plotly_utils.basevalidators as _bv


class YValidator(_bv.InfoArrayValidator):
    def __init__(self, plotly_name="y", parent_name="layout.polar.domain", **kwargs):
        super().__init__(
            plotly_name,
            parent_name,
            edit_type=kwargs.pop("edit_type", "plot"),
            items=kwargs.pop(
                "items",
                [
                    {"editType": "plot", "max": 1, "min": 0, "valType": "number"},
                    {"editType": "plot", "max": 1, "min": 0, "valType": "number"},
                ],
            ),
            **kwargs,
        )
