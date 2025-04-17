import _plotly_utils.basevalidators as _bv


class ValueminusValidator(_bv.NumberValidator):
    def __init__(
        self, plotly_name="valueminus", parent_name="scatter.error_x", **kwargs
    ):
        super().__init__(
            plotly_name,
            parent_name,
            edit_type=kwargs.pop("edit_type", "calc"),
            min=kwargs.pop("min", 0),
            **kwargs,
        )
