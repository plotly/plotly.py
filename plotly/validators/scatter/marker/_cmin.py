#                   --- THIS FILE IS AUTO-GENERATED ---
# Modifications will be overwitten the next time code generation run.

import _plotly_utils.basevalidators as _bv


class CminValidator(_bv.NumberValidator):
    def __init__(self, plotly_name="cmin", parent_name="scatter.marker", **kwargs):
        super().__init__(
            plotly_name,
            parent_name,
            edit_type=kwargs.pop("edit_type", "plot"),
            implied_edits=kwargs.pop("implied_edits", {"cauto": False}),
            **kwargs,
        )
