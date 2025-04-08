#                   --- THIS FILE IS AUTO-GENERATED ---
# Modifications will be overwitten the next time code generation run.

import _plotly_utils.basevalidators as _bv


class TextpositionValidator(_bv.EnumeratedValidator):
    def __init__(self, plotly_name="textposition", parent_name="bar", **kwargs):
        super().__init__(
            plotly_name,
            parent_name,
            array_ok=kwargs.pop("array_ok", True),
            edit_type=kwargs.pop("edit_type", "calc"),
            values=kwargs.pop("values", ["inside", "outside", "auto", "none"]),
            **kwargs,
        )
