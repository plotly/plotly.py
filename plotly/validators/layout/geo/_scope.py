#                   --- THIS FILE IS AUTO-GENERATED ---
# Modifications will be overwitten the next time code generation run.

import _plotly_utils.basevalidators as _bv


class ScopeValidator(_bv.EnumeratedValidator):
    def __init__(self, plotly_name="scope", parent_name="layout.geo", **kwargs):
        super().__init__(
            plotly_name,
            parent_name,
            edit_type=kwargs.pop("edit_type", "plot"),
            values=kwargs.pop(
                "values",
                [
                    "africa",
                    "asia",
                    "europe",
                    "north america",
                    "south america",
                    "usa",
                    "world",
                ],
            ),
            **kwargs,
        )
