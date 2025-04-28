#                   --- THIS FILE IS AUTO-GENERATED ---
# Modifications will be overwitten the next time code generation run.

import _plotly_utils.basevalidators as _bv


class Scatter3DValidator(_bv.CompoundArrayValidator):
    def __init__(
        self, plotly_name="scatter3d", parent_name="layout.template.data", **kwargs
    ):
        super().__init__(
            plotly_name,
            parent_name,
            data_class_str=kwargs.pop("data_class_str", "Scatter3d"),
            data_docs=kwargs.pop(
                "data_docs",
                """
""",
            ),
            **kwargs,
        )
