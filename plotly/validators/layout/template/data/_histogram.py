import _plotly_utils.basevalidators as _bv


class HistogramValidator(_bv.CompoundArrayValidator):
    def __init__(
        self, plotly_name="histogram", parent_name="layout.template.data", **kwargs
    ):
        super().__init__(
            plotly_name,
            parent_name,
            data_class_str=kwargs.pop("data_class_str", "Histogram"),
            data_docs=kwargs.pop(
                "data_docs",
                """
""",
            ),
            **kwargs,
        )
