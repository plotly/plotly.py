import _plotly_utils.basevalidators as _bv


class PrefixValidator(_bv.StringValidator):
    def __init__(self, plotly_name="prefix", parent_name="indicator.delta", **kwargs):
        super().__init__(
            plotly_name,
            parent_name,
            edit_type=kwargs.pop("edit_type", "plot"),
            **kwargs,
        )
