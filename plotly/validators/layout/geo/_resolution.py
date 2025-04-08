#                   --- THIS FILE IS AUTO-GENERATED ---
# Modifications will be overwitten the next time code generation run.

import _plotly_utils.basevalidators as _bv


class ResolutionValidator(_bv.EnumeratedValidator):
    def __init__(self, plotly_name="resolution", parent_name="layout.geo", **kwargs):
        super().__init__(
            plotly_name,
            parent_name,
            coerce_number=kwargs.pop("coerce_number", True),
            edit_type=kwargs.pop("edit_type", "plot"),
            values=kwargs.pop("values", [110, 50]),
            **kwargs,
        )
