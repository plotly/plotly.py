#                   --- THIS FILE IS AUTO-GENERATED ---
# Modifications will be overwitten the next time code generation run.

import _plotly_utils.basevalidators as _bv


class AutomarginValidator(_bv.FlaglistValidator):
    def __init__(self, plotly_name="automargin", parent_name="layout.xaxis", **kwargs):
        super().__init__(
            plotly_name,
            parent_name,
            edit_type=kwargs.pop("edit_type", "ticks"),
            extras=kwargs.pop("extras", [True, False]),
            flags=kwargs.pop(
                "flags", ["height", "width", "left", "right", "top", "bottom"]
            ),
            **kwargs,
        )
