import _plotly_utils.basevalidators as _bv


class ColorscaleValidator(_bv.ColorscaleValidator):
    def __init__(
        self, plotly_name="colorscale", parent_name="scatter.fillgradient", **kwargs
    ):
        super().__init__(
            plotly_name,
            parent_name,
            edit_type=kwargs.pop("edit_type", "style"),
            **kwargs,
        )
