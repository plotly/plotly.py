#                   --- THIS FILE IS AUTO-GENERATED ---
# Modifications will be overwitten the next time code generation run.

import _plotly_utils.basevalidators as _bv


class GroupclickValidator(_bv.EnumeratedValidator):
    def __init__(self, plotly_name="groupclick", parent_name="layout.legend", **kwargs):
        super().__init__(
            plotly_name,
            parent_name,
            edit_type=kwargs.pop("edit_type", "legend"),
            values=kwargs.pop("values", ["toggleitem", "togglegroup"]),
            **kwargs,
        )
