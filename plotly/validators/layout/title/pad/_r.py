#                   --- THIS FILE IS AUTO-GENERATED ---
# Modifications will be overwitten the next time code generation run.

import _plotly_utils.basevalidators as _bv


class RValidator(_bv.NumberValidator):
    def __init__(self, plotly_name="r", parent_name="layout.title.pad", **kwargs):
        super().__init__(
            plotly_name,
            parent_name,
            edit_type=kwargs.pop("edit_type", "layoutstyle"),
            **kwargs,
        )
