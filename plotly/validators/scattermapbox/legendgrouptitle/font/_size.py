#                   --- THIS FILE IS AUTO-GENERATED ---
# Modifications will be overwitten the next time code generation run.

import _plotly_utils.basevalidators as _bv


class SizeValidator(_bv.NumberValidator):
    def __init__(
        self,
        plotly_name="size",
        parent_name="scattermapbox.legendgrouptitle.font",
        **kwargs,
    ):
        super().__init__(
            plotly_name,
            parent_name,
            edit_type=kwargs.pop("edit_type", "style"),
            min=kwargs.pop("min", 1),
            **kwargs,
        )
