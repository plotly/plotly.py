import _plotly_utils.basevalidators as _bv


class YValidator(_bv.AnyValidator):
    def __init__(self, plotly_name="y", parent_name="layout.image", **kwargs):
        super().__init__(
            plotly_name,
            parent_name,
            edit_type=kwargs.pop("edit_type", "arraydraw"),
            **kwargs,
        )
