import _plotly_utils.basevalidators as _bv


class DistanceValidator(_bv.NumberValidator):
    def __init__(
        self, plotly_name="distance", parent_name="layout.geo.projection", **kwargs
    ):
        super().__init__(
            plotly_name,
            parent_name,
            edit_type=kwargs.pop("edit_type", "plot"),
            min=kwargs.pop("min", 1.001),
            **kwargs,
        )
