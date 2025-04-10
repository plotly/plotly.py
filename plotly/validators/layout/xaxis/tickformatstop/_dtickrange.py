#                   --- THIS FILE IS AUTO-GENERATED ---
# Modifications will be overwitten the next time code generation run.

import _plotly_utils.basevalidators as _bv


class DtickrangeValidator(_bv.InfoArrayValidator):
    def __init__(
        self,
        plotly_name="dtickrange",
        parent_name="layout.xaxis.tickformatstop",
        **kwargs,
    ):
        super().__init__(
            plotly_name,
            parent_name,
            edit_type=kwargs.pop("edit_type", "ticks"),
            items=kwargs.pop(
                "items",
                [
                    {"editType": "ticks", "valType": "any"},
                    {"editType": "ticks", "valType": "any"},
                ],
            ),
            **kwargs,
        )
