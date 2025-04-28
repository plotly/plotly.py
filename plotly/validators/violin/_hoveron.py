#                   --- THIS FILE IS AUTO-GENERATED ---
# Modifications will be overwitten the next time code generation run.

import _plotly_utils.basevalidators as _bv


class HoveronValidator(_bv.FlaglistValidator):
    def __init__(self, plotly_name="hoveron", parent_name="violin", **kwargs):
        super().__init__(
            plotly_name,
            parent_name,
            edit_type=kwargs.pop("edit_type", "style"),
            extras=kwargs.pop("extras", ["all"]),
            flags=kwargs.pop("flags", ["violins", "points", "kde"]),
            **kwargs,
        )
