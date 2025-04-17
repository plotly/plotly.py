import _plotly_utils.basevalidators as _bv


class ShapeValidator(_bv.EnumeratedValidator):
    def __init__(
        self, plotly_name="shape", parent_name="scatterternary.line", **kwargs
    ):
        super().__init__(
            plotly_name,
            parent_name,
            edit_type=kwargs.pop("edit_type", "plot"),
            values=kwargs.pop("values", ["linear", "spline"]),
            **kwargs,
        )
