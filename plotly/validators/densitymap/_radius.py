import _plotly_utils.basevalidators as _bv


class RadiusValidator(_bv.NumberValidator):
    def __init__(self, plotly_name="radius", parent_name="densitymap", **kwargs):
        super().__init__(
            plotly_name,
            parent_name,
            array_ok=kwargs.pop("array_ok", True),
            edit_type=kwargs.pop("edit_type", "plot"),
            min=kwargs.pop("min", 1),
            **kwargs,
        )
