#                   --- THIS FILE IS AUTO-GENERATED ---
# Modifications will be overwitten the next time code generation run.

import _plotly_utils.basevalidators as _bv


class HoverinfoValidator(_bv.FlaglistValidator):
    def __init__(
        self, plotly_name="hoverinfo", parent_name="choroplethmapbox", **kwargs
    ):
        super().__init__(
            plotly_name,
            parent_name,
            array_ok=kwargs.pop("array_ok", True),
            edit_type=kwargs.pop("edit_type", "calc"),
            extras=kwargs.pop("extras", ["all", "none", "skip"]),
            flags=kwargs.pop("flags", ["location", "z", "text", "name"]),
            **kwargs,
        )
