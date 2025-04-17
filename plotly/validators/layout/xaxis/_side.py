import _plotly_utils.basevalidators as _bv


class SideValidator(_bv.EnumeratedValidator):
    def __init__(self, plotly_name="side", parent_name="layout.xaxis", **kwargs):
        super().__init__(
            plotly_name,
            parent_name,
            edit_type=kwargs.pop("edit_type", "plot"),
            values=kwargs.pop("values", ["top", "bottom", "left", "right"]),
            **kwargs,
        )
