#                   --- THIS FILE IS AUTO-GENERATED ---
# Modifications will be overwitten the next time code generation run.

import _plotly_utils.basevalidators as _bv


class SymbolValidator(_bv.StringValidator):
    def __init__(
        self, plotly_name="symbol", parent_name="indicator.delta.increasing", **kwargs
    ):
        super().__init__(
            plotly_name,
            parent_name,
            edit_type=kwargs.pop("edit_type", "plot"),
            **kwargs,
        )
