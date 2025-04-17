import _plotly_utils.basevalidators as _bv


class XanchorValidator(_bv.AnyValidator):
    def __init__(self, plotly_name="xanchor", parent_name="layout.shape", **kwargs):
        super().__init__(
            plotly_name,
            parent_name,
            edit_type=kwargs.pop("edit_type", "calc+arraydraw"),
            **kwargs,
        )
