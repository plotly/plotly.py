#                   --- THIS FILE IS AUTO-GENERATED ---
# Modifications will be overwitten the next time code generation run.

import _plotly_utils.basevalidators as _bv


class LegendrankValidator(_bv.NumberValidator):
    def __init__(self, plotly_name="legendrank", parent_name="barpolar", **kwargs):
        super().__init__(
            plotly_name,
            parent_name,
            edit_type=kwargs.pop("edit_type", "style"),
            **kwargs,
        )
