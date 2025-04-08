#                   --- THIS FILE IS AUTO-GENERATED ---
# Modifications will be overwitten the next time code generation run.

import _plotly_utils.basevalidators as _bv


class LayerValidator(_bv.EnumeratedValidator):
    def __init__(self, plotly_name="layer", parent_name="layout.image", **kwargs):
        super().__init__(
            plotly_name,
            parent_name,
            edit_type=kwargs.pop("edit_type", "arraydraw"),
            values=kwargs.pop("values", ["below", "above"]),
            **kwargs,
        )
