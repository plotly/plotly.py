#                   --- THIS FILE IS AUTO-GENERATED ---
# Modifications will be overwitten the next time code generation run.

import _plotly_utils.basevalidators as _bv


class WidthValidator(_bv.NumberValidator):
    def __init__(self, plotly_name="width", parent_name="layout.shape.line", **kwargs):
        super().__init__(
            plotly_name,
            parent_name,
            anim=kwargs.pop("anim", True),
            edit_type=kwargs.pop("edit_type", "calc+arraydraw"),
            min=kwargs.pop("min", 0),
            **kwargs,
        )
