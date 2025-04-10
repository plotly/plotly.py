#                   --- THIS FILE IS AUTO-GENERATED ---
# Modifications will be overwitten the next time code generation run.

import _plotly_utils.basevalidators as _bv


class TextinfoValidator(_bv.FlaglistValidator):
    def __init__(self, plotly_name="textinfo", parent_name="funnelarea", **kwargs):
        super().__init__(
            plotly_name,
            parent_name,
            edit_type=kwargs.pop("edit_type", "calc"),
            extras=kwargs.pop("extras", ["none"]),
            flags=kwargs.pop("flags", ["label", "text", "value", "percent"]),
            **kwargs,
        )
