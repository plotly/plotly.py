import _plotly_utils.basevalidators as _bv


class CloseValidator(_bv.DataArrayValidator):
    def __init__(self, plotly_name="close", parent_name="candlestick", **kwargs):
        super().__init__(
            plotly_name,
            parent_name,
            edit_type=kwargs.pop("edit_type", "calc"),
            **kwargs,
        )
