import _plotly_utils.basevalidators as _bv


class ColorbarValidator(_bv.CompoundValidator):
    def __init__(
        self, plotly_name="colorbar", parent_name="choroplethmapbox", **kwargs
    ):
        super().__init__(
            plotly_name,
            parent_name,
            data_class_str=kwargs.pop("data_class_str", "ColorBar"),
            data_docs=kwargs.pop(
                "data_docs",
                """
""",
            ),
            **kwargs,
        )
