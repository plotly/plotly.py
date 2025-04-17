import _plotly_utils.basevalidators as _bv


class FillcolorValidator(_bv.ColorValidator):
    def __init__(self, plotly_name="fillcolor", parent_name="contour", **kwargs):
        super().__init__(
            plotly_name,
            parent_name,
            edit_type=kwargs.pop("edit_type", "calc"),
            colorscale_path=kwargs.pop("colorscale_path", "contour.colorscale"),
            **kwargs,
        )
