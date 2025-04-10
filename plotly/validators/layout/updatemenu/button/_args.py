#                   --- THIS FILE IS AUTO-GENERATED ---
# Modifications will be overwitten the next time code generation run.

import _plotly_utils.basevalidators as _bv


class ArgsValidator(_bv.InfoArrayValidator):
    def __init__(
        self, plotly_name="args", parent_name="layout.updatemenu.button", **kwargs
    ):
        super().__init__(
            plotly_name,
            parent_name,
            edit_type=kwargs.pop("edit_type", "arraydraw"),
            free_length=kwargs.pop("free_length", True),
            items=kwargs.pop(
                "items",
                [
                    {"editType": "arraydraw", "valType": "any"},
                    {"editType": "arraydraw", "valType": "any"},
                    {"editType": "arraydraw", "valType": "any"},
                ],
            ),
            **kwargs,
        )
