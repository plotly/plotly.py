import _plotly_utils.basevalidators as _bv


class TickmodeValidator(_bv.EnumeratedValidator):
    def __init__(
        self, plotly_name="tickmode", parent_name="treemap.marker.colorbar", **kwargs
    ):
        super().__init__(
            plotly_name,
            parent_name,
            edit_type=kwargs.pop("edit_type", "colorbars"),
            implied_edits=kwargs.pop("implied_edits", {}),
            values=kwargs.pop("values", ["auto", "linear", "array"]),
            **kwargs,
        )
