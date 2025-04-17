import _plotly_utils.basevalidators as _bv


class YanchorValidator(_bv.EnumeratedValidator):
    def __init__(
        self, plotly_name="yanchor", parent_name="treemap.marker.colorbar", **kwargs
    ):
        super().__init__(
            plotly_name,
            parent_name,
            edit_type=kwargs.pop("edit_type", "colorbars"),
            values=kwargs.pop("values", ["top", "middle", "bottom"]),
            **kwargs,
        )
