import _plotly_utils.basevalidators as _bv


class XperiodValidator(_bv.AnyValidator):
    def __init__(self, plotly_name="xperiod", parent_name="candlestick", **kwargs):
        super().__init__(
            plotly_name,
            parent_name,
            edit_type=kwargs.pop("edit_type", "calc"),
            **kwargs,
        )
