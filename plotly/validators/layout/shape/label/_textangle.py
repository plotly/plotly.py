#                   --- THIS FILE IS AUTO-GENERATED ---
# Modifications will be overwitten the next time code generation run.

import _plotly_utils.basevalidators as _bv


class TextangleValidator(_bv.AngleValidator):
    def __init__(
        self, plotly_name="textangle", parent_name="layout.shape.label", **kwargs
    ):
        super().__init__(
            plotly_name,
            parent_name,
            edit_type=kwargs.pop("edit_type", "calc+arraydraw"),
            **kwargs,
        )
