import _plotly_utils.basevalidators as _bv


class UnselectedValidator(_bv.CompoundValidator):
    def __init__(self, plotly_name="unselected", parent_name="scatterpolar", **kwargs):
        super().__init__(
            plotly_name,
            parent_name,
            data_class_str=kwargs.pop("data_class_str", "Unselected"),
            data_docs=kwargs.pop(
                "data_docs",
                """
""",
            ),
            **kwargs,
        )
