#                   --- THIS FILE IS AUTO-GENERATED ---
# Modifications will be overwitten the next time code generation run.

import _plotly_utils.basevalidators as _bv


class SideValidator(_bv.EnumeratedValidator):
    def __init__(
        self,
        plotly_name="side",
        parent_name="scatterternary.marker.colorbar.title",
        **kwargs,
    ):
        super().__init__(
            plotly_name,
            parent_name,
            edit_type=kwargs.pop("edit_type", "colorbars"),
            values=kwargs.pop("values", ["right", "top", "bottom"]),
            **kwargs,
        )
