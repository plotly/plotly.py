import _plotly_utils.basevalidators as _bv


class MaxzoomValidator(_bv.NumberValidator):
    def __init__(
        self, plotly_name="maxzoom", parent_name="scattermapbox.cluster", **kwargs
    ):
        super().__init__(
            plotly_name,
            parent_name,
            edit_type=kwargs.pop("edit_type", "calc"),
            max=kwargs.pop("max", 24),
            min=kwargs.pop("min", 0),
            **kwargs,
        )
