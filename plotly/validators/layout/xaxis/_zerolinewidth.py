import _plotly_utils.basevalidators as _bv


class ZerolinewidthValidator(_bv.NumberValidator):
    def __init__(
        self, plotly_name="zerolinewidth", parent_name="layout.xaxis", **kwargs
    ):
        super().__init__(
            plotly_name,
            parent_name,
            edit_type=kwargs.pop("edit_type", "ticks"),
            **kwargs,
        )
