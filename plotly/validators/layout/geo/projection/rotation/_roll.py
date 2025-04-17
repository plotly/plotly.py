import _plotly_utils.basevalidators as _bv


class RollValidator(_bv.NumberValidator):
    def __init__(
        self, plotly_name="roll", parent_name="layout.geo.projection.rotation", **kwargs
    ):
        super().__init__(
            plotly_name,
            parent_name,
            edit_type=kwargs.pop("edit_type", "plot"),
            **kwargs,
        )
