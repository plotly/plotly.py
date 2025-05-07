#                   --- THIS FILE IS AUTO-GENERATED ---
# Modifications will be overwitten the next time code generation run.

import _plotly_utils.basevalidators as _bv


class HovermodeValidator(_bv.EnumeratedValidator):
    def __init__(self, plotly_name="hovermode", parent_name="layout.scene", **kwargs):
        super().__init__(
            plotly_name,
            parent_name,
            edit_type=kwargs.pop("edit_type", "modebar"),
            values=kwargs.pop("values", ["closest", False]),
            **kwargs,
        )
