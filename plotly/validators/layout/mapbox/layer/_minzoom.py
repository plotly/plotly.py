#                   --- THIS FILE IS AUTO-GENERATED ---
# Modifications will be overwitten the next time code generation run.

import _plotly_utils.basevalidators as _bv


class MinzoomValidator(_bv.NumberValidator):
    def __init__(
        self, plotly_name="minzoom", parent_name="layout.mapbox.layer", **kwargs
    ):
        super().__init__(
            plotly_name,
            parent_name,
            edit_type=kwargs.pop("edit_type", "plot"),
            max=kwargs.pop("max", 24),
            min=kwargs.pop("min", 0),
            **kwargs,
        )
