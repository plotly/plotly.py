#                   --- THIS FILE IS AUTO-GENERATED ---
# Modifications will be overwitten the next time code generation run.

import _plotly_utils.basevalidators as _bv


class RoworderValidator(_bv.EnumeratedValidator):
    def __init__(self, plotly_name="roworder", parent_name="layout.grid", **kwargs):
        super().__init__(
            plotly_name,
            parent_name,
            edit_type=kwargs.pop("edit_type", "plot"),
            values=kwargs.pop("values", ["top to bottom", "bottom to top"]),
            **kwargs,
        )
