import _plotly_utils.basevalidators as _bv


class HoverinfoValidator(_bv.EnumeratedValidator):
    def __init__(self, plotly_name="hoverinfo", parent_name="sankey.link", **kwargs):
        super().__init__(
            plotly_name,
            parent_name,
            edit_type=kwargs.pop("edit_type", "calc"),
            values=kwargs.pop("values", ["all", "none", "skip"]),
            **kwargs,
        )
