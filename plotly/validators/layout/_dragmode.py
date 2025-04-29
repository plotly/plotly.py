#                   --- THIS FILE IS AUTO-GENERATED ---
# Modifications will be overwitten the next time code generation run.

import _plotly_utils.basevalidators as _bv


class DragmodeValidator(_bv.EnumeratedValidator):
    def __init__(self, plotly_name="dragmode", parent_name="layout", **kwargs):
        super().__init__(
            plotly_name,
            parent_name,
            edit_type=kwargs.pop("edit_type", "modebar"),
            values=kwargs.pop(
                "values",
                [
                    "zoom",
                    "pan",
                    "select",
                    "lasso",
                    "drawclosedpath",
                    "drawopenpath",
                    "drawline",
                    "drawrect",
                    "drawcircle",
                    "orbit",
                    "turntable",
                    False,
                ],
            ),
            **kwargs,
        )
