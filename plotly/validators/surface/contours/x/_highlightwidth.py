import _plotly_utils.basevalidators as _bv


class HighlightwidthValidator(_bv.NumberValidator):
    def __init__(
        self, plotly_name="highlightwidth", parent_name="surface.contours.x", **kwargs
    ):
        super().__init__(
            plotly_name,
            parent_name,
            edit_type=kwargs.pop("edit_type", "calc"),
            max=kwargs.pop("max", 16),
            min=kwargs.pop("min", 1),
            **kwargs,
        )
