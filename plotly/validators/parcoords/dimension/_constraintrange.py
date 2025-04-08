#                   --- THIS FILE IS AUTO-GENERATED ---
# Modifications will be overwitten the next time code generation run.

import _plotly_utils.basevalidators as _bv


class ConstraintrangeValidator(_bv.InfoArrayValidator):
    def __init__(
        self, plotly_name="constraintrange", parent_name="parcoords.dimension", **kwargs
    ):
        super().__init__(
            plotly_name,
            parent_name,
            dimensions=kwargs.pop("dimensions", "1-2"),
            edit_type=kwargs.pop("edit_type", "plot"),
            free_length=kwargs.pop("free_length", True),
            items=kwargs.pop(
                "items",
                [
                    {"editType": "plot", "valType": "any"},
                    {"editType": "plot", "valType": "any"},
                ],
            ),
            **kwargs,
        )
