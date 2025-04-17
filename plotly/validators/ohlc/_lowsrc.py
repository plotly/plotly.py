import _plotly_utils.basevalidators as _bv


class LowsrcValidator(_bv.SrcValidator):
    def __init__(self, plotly_name="lowsrc", parent_name="ohlc", **kwargs):
        super().__init__(
            plotly_name,
            parent_name,
            edit_type=kwargs.pop("edit_type", "none"),
            **kwargs,
        )
