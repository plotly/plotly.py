import _plotly_utils.basevalidators as _bv


class SizeValidator(_bv.NumberValidator):
    def __init__(
        self, plotly_name="size", parent_name="scatterternary.hoverlabel.font", **kwargs
    ):
        super().__init__(
            plotly_name,
            parent_name,
            array_ok=kwargs.pop("array_ok", True),
            edit_type=kwargs.pop("edit_type", "none"),
            min=kwargs.pop("min", 1),
            **kwargs,
        )
