import _plotly_utils.basevalidators as _bv


class HighlightcolorValidator(_bv.ColorValidator):
    def __init__(
        self, plotly_name="highlightcolor", parent_name="surface.contours.y", **kwargs
    ):
        super().__init__(
            plotly_name,
            parent_name,
            edit_type=kwargs.pop("edit_type", "calc"),
            **kwargs,
        )
