#                   --- THIS FILE IS AUTO-GENERATED ---
# Modifications will be overwitten the next time code generation run.

import _plotly_utils.basevalidators as _bv


class OutlinecolorValidator(_bv.ColorValidator):
    def __init__(
        self, plotly_name="outlinecolor", parent_name="layout.map.layer.fill", **kwargs
    ):
        super().__init__(
            plotly_name,
            parent_name,
            edit_type=kwargs.pop("edit_type", "plot"),
            **kwargs,
        )
