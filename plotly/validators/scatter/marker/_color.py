import _plotly_utils.basevalidators as _bv


class ColorValidator(_bv.ColorValidator):
    def __init__(self, plotly_name="color", parent_name="scatter.marker", **kwargs):
        super().__init__(
            plotly_name,
            parent_name,
            anim=kwargs.pop("anim", True),
            array_ok=kwargs.pop("array_ok", True),
            edit_type=kwargs.pop("edit_type", "style"),
            colorscale_path=kwargs.pop("colorscale_path", "scatter.marker.colorscale"),
            **kwargs,
        )
