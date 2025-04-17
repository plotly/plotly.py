#                   --- THIS FILE IS AUTO-GENERATED ---
# Modifications will be overwitten the next time code generation run.

import _plotly_utils.basevalidators as _bv


class FillruleValidator(_bv.EnumeratedValidator):
    def __init__(self, plotly_name="fillrule", parent_name="layout.newshape", **kwargs):
        super().__init__(
            plotly_name,
            parent_name,
            edit_type=kwargs.pop("edit_type", "none"),
            values=kwargs.pop("values", ["evenodd", "nonzero"]),
            **kwargs,
        )
