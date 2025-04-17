import _plotly_utils.basevalidators as _bv


class Xperiod0Validator(_bv.AnyValidator):
    def __init__(self, plotly_name="xperiod0", parent_name="candlestick", **kwargs):
        super().__init__(
            plotly_name,
            parent_name,
            edit_type=kwargs.pop("edit_type", "calc"),
            **kwargs,
        )
