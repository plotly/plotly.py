import _plotly_utils.basevalidators as _bv


class CornerradiusValidator(_bv.NumberValidator):
    def __init__(
        self, plotly_name="cornerradius", parent_name="treemap.marker", **kwargs
    ):
        super().__init__(
            plotly_name,
            parent_name,
            edit_type=kwargs.pop("edit_type", "plot"),
            min=kwargs.pop("min", 0),
            **kwargs,
        )
