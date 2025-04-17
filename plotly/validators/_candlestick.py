import _plotly_utils.basevalidators as _bv


class CandlestickValidator(_bv.CompoundValidator):
    def __init__(self, plotly_name="candlestick", parent_name="", **kwargs):
        super().__init__(
            plotly_name,
            parent_name,
            data_class_str=kwargs.pop("data_class_str", "Candlestick"),
            data_docs=kwargs.pop(
                "data_docs",
                """
""",
            ),
            **kwargs,
        )
