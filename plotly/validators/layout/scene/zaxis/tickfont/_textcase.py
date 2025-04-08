#                   --- THIS FILE IS AUTO-GENERATED ---
# Modifications will be overwitten the next time code generation run.

import _plotly_utils.basevalidators as _bv


class TextcaseValidator(_bv.EnumeratedValidator):
    def __init__(
        self,
        plotly_name="textcase",
        parent_name="layout.scene.zaxis.tickfont",
        **kwargs,
    ):
        super().__init__(
            plotly_name,
            parent_name,
            edit_type=kwargs.pop("edit_type", "plot"),
            values=kwargs.pop("values", ["normal", "word caps", "upper", "lower"]),
            **kwargs,
        )
