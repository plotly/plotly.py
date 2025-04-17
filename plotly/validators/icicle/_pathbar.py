import _plotly_utils.basevalidators as _bv


class PathbarValidator(_bv.CompoundValidator):
    def __init__(self, plotly_name="pathbar", parent_name="icicle", **kwargs):
        super().__init__(
            plotly_name,
            parent_name,
            data_class_str=kwargs.pop("data_class_str", "Pathbar"),
            data_docs=kwargs.pop(
                "data_docs",
                """
""",
            ),
            **kwargs,
        )
