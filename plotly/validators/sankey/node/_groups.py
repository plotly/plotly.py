#                   --- THIS FILE IS AUTO-GENERATED ---
# Modifications will be overwitten the next time code generation run.

import _plotly_utils.basevalidators as _bv


class GroupsValidator(_bv.InfoArrayValidator):
    def __init__(self, plotly_name="groups", parent_name="sankey.node", **kwargs):
        super().__init__(
            plotly_name,
            parent_name,
            dimensions=kwargs.pop("dimensions", 2),
            edit_type=kwargs.pop("edit_type", "calc"),
            free_length=kwargs.pop("free_length", True),
            implied_edits=kwargs.pop("implied_edits", {"x": [], "y": []}),
            items=kwargs.pop("items", {"editType": "calc", "valType": "number"}),
            **kwargs,
        )
