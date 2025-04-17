import _plotly_utils.basevalidators as _bv


class StandoffValidator(_bv.NumberValidator):
    def __init__(
        self, plotly_name="standoff", parent_name="layout.xaxis.title", **kwargs
    ):
        super().__init__(
            plotly_name,
            parent_name,
            edit_type=kwargs.pop("edit_type", "ticks"),
            min=kwargs.pop("min", 0),
            **kwargs,
        )
