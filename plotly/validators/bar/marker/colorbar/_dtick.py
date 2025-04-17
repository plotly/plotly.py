import _plotly_utils.basevalidators as _bv


class DtickValidator(_bv.AnyValidator):
    def __init__(
        self, plotly_name="dtick", parent_name="bar.marker.colorbar", **kwargs
    ):
        super().__init__(
            plotly_name,
            parent_name,
            edit_type=kwargs.pop("edit_type", "colorbars"),
            implied_edits=kwargs.pop("implied_edits", {"tickmode": "linear"}),
            **kwargs,
        )
