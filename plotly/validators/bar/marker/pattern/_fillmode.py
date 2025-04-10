#                   --- THIS FILE IS AUTO-GENERATED ---
# Modifications will be overwitten the next time code generation run.

import _plotly_utils.basevalidators as _bv


class FillmodeValidator(_bv.EnumeratedValidator):
    def __init__(
        self, plotly_name="fillmode", parent_name="bar.marker.pattern", **kwargs
    ):
        super().__init__(
            plotly_name,
            parent_name,
            edit_type=kwargs.pop("edit_type", "style"),
            values=kwargs.pop("values", ["replace", "overlay"]),
            **kwargs,
        )
