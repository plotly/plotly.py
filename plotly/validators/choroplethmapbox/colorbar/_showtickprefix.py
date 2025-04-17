#                   --- THIS FILE IS AUTO-GENERATED ---
# Modifications will be overwitten the next time code generation run.

import _plotly_utils.basevalidators as _bv


class ShowtickprefixValidator(_bv.EnumeratedValidator):
    def __init__(
        self,
        plotly_name="showtickprefix",
        parent_name="choroplethmapbox.colorbar",
        **kwargs,
    ):
        super().__init__(
            plotly_name,
            parent_name,
            edit_type=kwargs.pop("edit_type", "colorbars"),
            values=kwargs.pop("values", ["all", "first", "last", "none"]),
            **kwargs,
        )
