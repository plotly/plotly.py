import _plotly_utils.basevalidators as _bv


class YaxisValidator(_bv.CompoundValidator):
    def __init__(
        self, plotly_name="yaxis", parent_name="layout.xaxis.rangeslider", **kwargs
    ):
        super().__init__(
            plotly_name,
            parent_name,
            data_class_str=kwargs.pop("data_class_str", "YAxis"),
            data_docs=kwargs.pop(
                "data_docs",
                """
""",
            ),
            **kwargs,
        )
