#                   --- THIS FILE IS AUTO-GENERATED ---
# Modifications will be overwitten the next time code generation run.

import _plotly_utils.basevalidators as _bv


class OutlierwidthValidator(_bv.NumberValidator):
    def __init__(
        self, plotly_name="outlierwidth", parent_name="box.marker.line", **kwargs
    ):
        super().__init__(
            plotly_name,
            parent_name,
            edit_type=kwargs.pop("edit_type", "style"),
            min=kwargs.pop("min", 0),
            **kwargs,
        )
