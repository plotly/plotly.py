import _plotly_utils.basevalidators as _bv


class ShowscaleValidator(_bv.BooleanValidator):
    def __init__(
        self, plotly_name="showscale", parent_name="scattercarpet.marker", **kwargs
    ):
        super().__init__(
            plotly_name,
            parent_name,
            edit_type=kwargs.pop("edit_type", "calc"),
            **kwargs,
        )
