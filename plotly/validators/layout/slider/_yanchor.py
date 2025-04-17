import _plotly_utils.basevalidators as _bv


class YanchorValidator(_bv.EnumeratedValidator):
    def __init__(self, plotly_name="yanchor", parent_name="layout.slider", **kwargs):
        super().__init__(
            plotly_name,
            parent_name,
            edit_type=kwargs.pop("edit_type", "arraydraw"),
            values=kwargs.pop("values", ["auto", "top", "middle", "bottom"]),
            **kwargs,
        )
