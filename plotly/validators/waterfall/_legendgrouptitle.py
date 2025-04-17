import _plotly_utils.basevalidators as _bv


class LegendgrouptitleValidator(_bv.CompoundValidator):
    def __init__(
        self, plotly_name="legendgrouptitle", parent_name="waterfall", **kwargs
    ):
        super().__init__(
            plotly_name,
            parent_name,
            data_class_str=kwargs.pop("data_class_str", "Legendgrouptitle"),
            data_docs=kwargs.pop(
                "data_docs",
                """
""",
            ),
            **kwargs,
        )
