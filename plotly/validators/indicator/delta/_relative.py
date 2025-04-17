import _plotly_utils.basevalidators as _bv


class RelativeValidator(_bv.BooleanValidator):
    def __init__(self, plotly_name="relative", parent_name="indicator.delta", **kwargs):
        super().__init__(
            plotly_name,
            parent_name,
            edit_type=kwargs.pop("edit_type", "plot"),
            **kwargs,
        )
