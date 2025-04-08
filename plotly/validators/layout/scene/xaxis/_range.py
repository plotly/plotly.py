#                   --- THIS FILE IS AUTO-GENERATED ---
# Modifications will be overwitten the next time code generation run.

import _plotly_utils.basevalidators as _bv


class RangeValidator(_bv.InfoArrayValidator):
    def __init__(self, plotly_name="range", parent_name="layout.scene.xaxis", **kwargs):
        super().__init__(
            plotly_name,
            parent_name,
            anim=kwargs.pop("anim", False),
            edit_type=kwargs.pop("edit_type", "plot"),
            implied_edits=kwargs.pop("implied_edits", {"autorange": False}),
            items=kwargs.pop(
                "items",
                [
                    {
                        "editType": "plot",
                        "impliedEdits": {"^autorange": False},
                        "valType": "any",
                    },
                    {
                        "editType": "plot",
                        "impliedEdits": {"^autorange": False},
                        "valType": "any",
                    },
                ],
            ),
            **kwargs,
        )
