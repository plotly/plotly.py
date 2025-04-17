import _plotly_utils.basevalidators as _bv


class GradientValidator(_bv.CompoundValidator):
    def __init__(
        self, plotly_name="gradient", parent_name="scattergeo.marker", **kwargs
    ):
        super().__init__(
            plotly_name,
            parent_name,
            data_class_str=kwargs.pop("data_class_str", "Gradient"),
            data_docs=kwargs.pop(
                "data_docs",
                """
""",
            ),
            **kwargs,
        )
