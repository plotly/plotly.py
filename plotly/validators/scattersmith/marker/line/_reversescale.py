import _plotly_utils.basevalidators as _bv


class ReversescaleValidator(_bv.BooleanValidator):
    def __init__(
        self,
        plotly_name="reversescale",
        parent_name="scattersmith.marker.line",
        **kwargs,
    ):
        super().__init__(
            plotly_name,
            parent_name,
            edit_type=kwargs.pop("edit_type", "plot"),
            **kwargs,
        )
