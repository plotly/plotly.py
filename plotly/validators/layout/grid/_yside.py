import _plotly_utils.basevalidators as _bv


class YsideValidator(_bv.EnumeratedValidator):
    def __init__(self, plotly_name="yside", parent_name="layout.grid", **kwargs):
        super().__init__(
            plotly_name,
            parent_name,
            edit_type=kwargs.pop("edit_type", "plot"),
            values=kwargs.pop("values", ["left", "left plot", "right plot", "right"]),
            **kwargs,
        )
