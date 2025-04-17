import _plotly_utils.basevalidators as _bv


class ScattergeoValidator(_bv.CompoundValidator):
    def __init__(self, plotly_name="scattergeo", parent_name="", **kwargs):
        super().__init__(
            plotly_name,
            parent_name,
            data_class_str=kwargs.pop("data_class_str", "Scattergeo"),
            data_docs=kwargs.pop(
                "data_docs",
                """
""",
            ),
            **kwargs,
        )
