import _plotly_utils.basevalidators as _bv


class StandoffValidator(_bv.NumberValidator):
    def __init__(
        self, plotly_name="standoff", parent_name="scattersmith.marker", **kwargs
    ):
        super().__init__(
            plotly_name,
            parent_name,
            array_ok=kwargs.pop("array_ok", True),
            edit_type=kwargs.pop("edit_type", "plot"),
            min=kwargs.pop("min", 0),
            **kwargs,
        )
