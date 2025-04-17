import _plotly_utils.basevalidators as _bv


class TicksuffixValidator(_bv.StringValidator):
    def __init__(self, plotly_name="ticksuffix", parent_name="layout.yaxis", **kwargs):
        super().__init__(
            plotly_name,
            parent_name,
            edit_type=kwargs.pop("edit_type", "ticks"),
            **kwargs,
        )
