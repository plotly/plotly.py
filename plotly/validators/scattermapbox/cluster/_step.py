import _plotly_utils.basevalidators as _bv


class StepValidator(_bv.NumberValidator):
    def __init__(
        self, plotly_name="step", parent_name="scattermapbox.cluster", **kwargs
    ):
        super().__init__(
            plotly_name,
            parent_name,
            array_ok=kwargs.pop("array_ok", True),
            edit_type=kwargs.pop("edit_type", "calc"),
            min=kwargs.pop("min", -1),
            **kwargs,
        )
