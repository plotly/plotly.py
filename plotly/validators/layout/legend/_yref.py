#                   --- THIS FILE IS AUTO-GENERATED ---
# Modifications will be overwitten the next time code generation run.

import _plotly_utils.basevalidators as _bv


class YrefValidator(_bv.EnumeratedValidator):
    def __init__(self, plotly_name="yref", parent_name="layout.legend", **kwargs):
        super().__init__(
            plotly_name,
            parent_name,
            edit_type=kwargs.pop("edit_type", "layoutstyle"),
            values=kwargs.pop("values", ["container", "paper"]),
            **kwargs,
        )
