#                   --- THIS FILE IS AUTO-GENERATED ---
# Modifications will be overwitten the next time code generation run.

import _plotly_utils.basevalidators as _bv


class XaxesValidator(_bv.InfoArrayValidator):
    def __init__(self, plotly_name="xaxes", parent_name="splom", **kwargs):
        super().__init__(
            plotly_name,
            parent_name,
            edit_type=kwargs.pop("edit_type", "calc"),
            free_length=kwargs.pop("free_length", True),
            items=kwargs.pop(
                "items",
                {
                    "editType": "plot",
                    "regex": "/^x([2-9]|[1-9][0-9]+)?( domain)?$/",
                    "valType": "subplotid",
                },
            ),
            **kwargs,
        )
