import _plotly_utils.basevalidators


class ModeValidator(_plotly_utils.basevalidators.EnumeratedValidator):
    def __init__(self, plotly_name="mode", parent_name="layout.uniformtext", **kwargs):
        super(ModeValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "plot"),
            role=kwargs.pop("role", "info"),
            values=kwargs.pop("values", [False, "hide", "show"]),
            **kwargs
        )


import _plotly_utils.basevalidators


class MinsizeValidator(_plotly_utils.basevalidators.NumberValidator):
    def __init__(
        self, plotly_name="minsize", parent_name="layout.uniformtext", **kwargs
    ):
        super(MinsizeValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "plot"),
            min=kwargs.pop("min", 0),
            role=kwargs.pop("role", "info"),
            **kwargs
        )
