import _plotly_utils.basevalidators as _bv


class EndValidator(_bv.NumberValidator):
    def __init__(self, plotly_name="end", parent_name="surface.contours.x", **kwargs):
        super().__init__(
            plotly_name,
            parent_name,
            edit_type=kwargs.pop("edit_type", "calc"),
            **kwargs,
        )
