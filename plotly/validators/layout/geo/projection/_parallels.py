#                   --- THIS FILE IS AUTO-GENERATED ---
# Modifications will be overwitten the next time code generation run.

import _plotly_utils.basevalidators as _bv


class ParallelsValidator(_bv.InfoArrayValidator):
    def __init__(
        self, plotly_name="parallels", parent_name="layout.geo.projection", **kwargs
    ):
        super().__init__(
            plotly_name,
            parent_name,
            edit_type=kwargs.pop("edit_type", "plot"),
            items=kwargs.pop(
                "items",
                [
                    {"editType": "plot", "valType": "number"},
                    {"editType": "plot", "valType": "number"},
                ],
            ),
            **kwargs,
        )
