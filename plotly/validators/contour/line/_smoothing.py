import _plotly_utils.basevalidators as _bv


class SmoothingValidator(_bv.NumberValidator):
    def __init__(self, plotly_name="smoothing", parent_name="contour.line", **kwargs):
        super().__init__(
            plotly_name,
            parent_name,
            edit_type=kwargs.pop("edit_type", "plot"),
            max=kwargs.pop("max", 1.3),
            min=kwargs.pop("min", 0),
            **kwargs,
        )
