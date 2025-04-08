#                   --- THIS FILE IS AUTO-GENERATED ---
# Modifications will be overwitten the next time code generation run.

import _plotly_utils.basevalidators as _bv


class GroupnormValidator(_bv.EnumeratedValidator):
    def __init__(self, plotly_name="groupnorm", parent_name="scatter", **kwargs):
        super().__init__(
            plotly_name,
            parent_name,
            edit_type=kwargs.pop("edit_type", "calc"),
            values=kwargs.pop("values", ["", "fraction", "percent"]),
            **kwargs,
        )
