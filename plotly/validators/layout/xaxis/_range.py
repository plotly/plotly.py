#                   --- THIS FILE IS AUTO-GENERATED ---
# Modifications will be overwitten the next time code generation run.

import _plotly_utils.basevalidators as _bv


class RangeValidator(_bv.InfoArrayValidator):
    def __init__(self, plotly_name="range", parent_name="layout.xaxis", **kwargs):
        super().__init__(
            plotly_name,
            parent_name,
            anim=kwargs.pop("anim", True),
            edit_type=kwargs.pop("edit_type", "axrange"),
            implied_edits=kwargs.pop("implied_edits", {"autorange": False}),
            items=kwargs.pop(
                "items",
                [
                    {
                        "anim": True,
                        "editType": "axrange",
                        "impliedEdits": {"^autorange": False},
                        "valType": "any",
                    },
                    {
                        "anim": True,
                        "editType": "axrange",
                        "impliedEdits": {"^autorange": False},
                        "valType": "any",
                    },
                ],
            ),
            **kwargs,
        )
