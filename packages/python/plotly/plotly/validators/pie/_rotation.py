import _plotly_utils.basevalidators


class RotationValidator(_plotly_utils.basevalidators.NumberValidator):
    def __init__(self, plotly_name="rotation", parent_name="pie", **kwargs):
        super(RotationValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "calc"),
            max=kwargs.pop("max", 360),
            min=kwargs.pop("min", -360),
            **kwargs,
        )
