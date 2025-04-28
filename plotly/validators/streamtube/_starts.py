#                   --- THIS FILE IS AUTO-GENERATED ---
# Modifications will be overwitten the next time code generation run.

import _plotly_utils.basevalidators as _bv


class StartsValidator(_bv.CompoundValidator):
    def __init__(self, plotly_name="starts", parent_name="streamtube", **kwargs):
        super().__init__(
            plotly_name,
            parent_name,
            data_class_str=kwargs.pop("data_class_str", "Starts"),
            data_docs=kwargs.pop(
                "data_docs",
                """
""",
            ),
            **kwargs,
        )
