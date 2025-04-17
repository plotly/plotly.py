import _plotly_utils.basevalidators as _bv


class ScatterpolarValidator(_bv.CompoundValidator):
    def __init__(self, plotly_name="scatterpolar", parent_name="", **kwargs):
        super().__init__(
            plotly_name,
            parent_name,
            data_class_str=kwargs.pop("data_class_str", "Scatterpolar"),
            data_docs=kwargs.pop(
                "data_docs",
                """
""",
            ),
            **kwargs,
        )
