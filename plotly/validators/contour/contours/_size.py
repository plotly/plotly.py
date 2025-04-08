#                   --- THIS FILE IS AUTO-GENERATED ---
# Modifications will be overwitten the next time code generation run.

import _plotly_utils.basevalidators as _bv


class SizeValidator(_bv.NumberValidator):
    def __init__(self, plotly_name="size", parent_name="contour.contours", **kwargs):
        super().__init__(
            plotly_name,
            parent_name,
            edit_type=kwargs.pop("edit_type", "plot"),
            implied_edits=kwargs.pop("implied_edits", {"^autocontour": False}),
            min=kwargs.pop("min", 0),
            **kwargs,
        )
