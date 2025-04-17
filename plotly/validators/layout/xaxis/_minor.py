import _plotly_utils.basevalidators as _bv


class MinorValidator(_bv.CompoundValidator):
    def __init__(self, plotly_name="minor", parent_name="layout.xaxis", **kwargs):
        super().__init__(
            plotly_name,
            parent_name,
            data_class_str=kwargs.pop("data_class_str", "Minor"),
            data_docs=kwargs.pop(
                "data_docs",
                """
""",
            ),
            **kwargs,
        )
