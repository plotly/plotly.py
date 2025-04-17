import _plotly_utils.basevalidators as _bv


class WeightValidator(_bv.IntegerValidator):
    def __init__(
        self,
        plotly_name="weight",
        parent_name="scatterternary.hoverlabel.font",
        **kwargs,
    ):
        super().__init__(
            plotly_name,
            parent_name,
            array_ok=kwargs.pop("array_ok", True),
            edit_type=kwargs.pop("edit_type", "none"),
            extras=kwargs.pop("extras", ["normal", "bold"]),
            max=kwargs.pop("max", 1000),
            min=kwargs.pop("min", 1),
            **kwargs,
        )
