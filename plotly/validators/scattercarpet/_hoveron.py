#                   --- THIS FILE IS AUTO-GENERATED ---
# Modifications will be overwitten the next time code generation run.

import _plotly_utils.basevalidators as _bv


class HoveronValidator(_bv.FlaglistValidator):
    def __init__(self, plotly_name="hoveron", parent_name="scattercarpet", **kwargs):
        super().__init__(
            plotly_name,
            parent_name,
            edit_type=kwargs.pop("edit_type", "style"),
            flags=kwargs.pop("flags", ["points", "fills"]),
            **kwargs,
        )
