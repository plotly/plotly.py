#                   --- THIS FILE IS AUTO-GENERATED ---
# Modifications will be overwitten the next time code generation run.

import _plotly_utils.basevalidators as _bv


class RangeValidator(_bv.InfoArrayValidator):
    def __init__(
        self, plotly_name="range", parent_name="layout.xaxis.rangeslider", **kwargs
    ):
        super().__init__(
            plotly_name,
            parent_name,
            edit_type=kwargs.pop("edit_type", "calc"),
            implied_edits=kwargs.pop("implied_edits", {"autorange": False}),
            items=kwargs.pop(
                "items",
                [
                    {
                        "editType": "calc",
                        "impliedEdits": {"^autorange": False},
                        "valType": "any",
                    },
                    {
                        "editType": "calc",
                        "impliedEdits": {"^autorange": False},
                        "valType": "any",
                    },
                ],
            ),
            **kwargs,
        )
