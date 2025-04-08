#                   --- THIS FILE IS AUTO-GENERATED ---
# Modifications will be overwitten the next time code generation run.

import _plotly_utils.basevalidators as _bv


class CategoryorderValidator(_bv.EnumeratedValidator):
    def __init__(
        self, plotly_name="categoryorder", parent_name="layout.scene.zaxis", **kwargs
    ):
        super().__init__(
            plotly_name,
            parent_name,
            edit_type=kwargs.pop("edit_type", "plot"),
            values=kwargs.pop(
                "values",
                [
                    "trace",
                    "category ascending",
                    "category descending",
                    "array",
                    "total ascending",
                    "total descending",
                    "min ascending",
                    "min descending",
                    "max ascending",
                    "max descending",
                    "sum ascending",
                    "sum descending",
                    "mean ascending",
                    "mean descending",
                    "geometric mean ascending",
                    "geometric mean descending",
                    "median ascending",
                    "median descending",
                ],
            ),
            **kwargs,
        )
