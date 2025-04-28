#                   --- THIS FILE IS AUTO-GENERATED ---
# Modifications will be overwitten the next time code generation run.

import _plotly_utils.basevalidators as _bv


class TypeValidator(_bv.EnumeratedValidator):
    def __init__(self, plotly_name="type", parent_name="layout.shape", **kwargs):
        super().__init__(
            plotly_name,
            parent_name,
            edit_type=kwargs.pop("edit_type", "calc+arraydraw"),
            values=kwargs.pop("values", ["circle", "rect", "path", "line"]),
            **kwargs,
        )
