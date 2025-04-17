import _plotly_utils.basevalidators as _bv


class BordercolorValidator(_bv.ColorValidator):
    def __init__(
        self,
        plotly_name="bordercolor",
        parent_name="scattergl.marker.colorbar",
        **kwargs,
    ):
        super().__init__(
            plotly_name,
            parent_name,
            edit_type=kwargs.pop("edit_type", "calc"),
            **kwargs,
        )
