#                   --- THIS FILE IS AUTO-GENERATED ---
# Modifications will be overwitten the next time code generation run.

import _plotly_utils.basevalidators as _bv


class PointposValidator(_bv.NumberValidator):
    def __init__(self, plotly_name="pointpos", parent_name="box", **kwargs):
        super().__init__(
            plotly_name,
            parent_name,
            edit_type=kwargs.pop("edit_type", "calc"),
            max=kwargs.pop("max", 2),
            min=kwargs.pop("min", -2),
            **kwargs,
        )
