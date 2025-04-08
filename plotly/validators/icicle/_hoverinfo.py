#                   --- THIS FILE IS AUTO-GENERATED ---
# Modifications will be overwitten the next time code generation run.

import _plotly_utils.basevalidators as _bv


class HoverinfoValidator(_bv.FlaglistValidator):
    def __init__(self, plotly_name="hoverinfo", parent_name="icicle", **kwargs):
        super().__init__(
            plotly_name,
            parent_name,
            array_ok=kwargs.pop("array_ok", True),
            edit_type=kwargs.pop("edit_type", "none"),
            extras=kwargs.pop("extras", ["all", "none", "skip"]),
            flags=kwargs.pop(
                "flags",
                [
                    "label",
                    "text",
                    "value",
                    "name",
                    "current path",
                    "percent root",
                    "percent entry",
                    "percent parent",
                ],
            ),
            **kwargs,
        )
