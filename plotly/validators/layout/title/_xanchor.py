import _plotly_utils.basevalidators as _bv


class XanchorValidator(_bv.EnumeratedValidator):
    def __init__(self, plotly_name="xanchor", parent_name="layout.title", **kwargs):
        super().__init__(
            plotly_name,
            parent_name,
            edit_type=kwargs.pop("edit_type", "layoutstyle"),
            values=kwargs.pop("values", ["auto", "left", "center", "right"]),
            **kwargs,
        )
