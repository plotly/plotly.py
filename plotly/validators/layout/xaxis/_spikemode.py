#                   --- THIS FILE IS AUTO-GENERATED ---
# Modifications will be overwitten the next time code generation run.

import _plotly_utils.basevalidators as _bv


class SpikemodeValidator(_bv.FlaglistValidator):
    def __init__(self, plotly_name="spikemode", parent_name="layout.xaxis", **kwargs):
        super().__init__(
            plotly_name,
            parent_name,
            edit_type=kwargs.pop("edit_type", "none"),
            flags=kwargs.pop("flags", ["toaxis", "across", "marker"]),
            **kwargs,
        )
