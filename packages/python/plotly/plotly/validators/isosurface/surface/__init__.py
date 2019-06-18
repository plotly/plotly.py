import _plotly_utils.basevalidators


class ShowValidator(_plotly_utils.basevalidators.BooleanValidator):
    def __init__(self, plotly_name="show", parent_name="isosurface.surface", **kwargs):
        super(ShowValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "calc"),
            role=kwargs.pop("role", "info"),
            **kwargs
        )


import _plotly_utils.basevalidators


class PatternValidator(_plotly_utils.basevalidators.FlaglistValidator):
    def __init__(
        self, plotly_name="pattern", parent_name="isosurface.surface", **kwargs
    ):
        super(PatternValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "calc"),
            extras=kwargs.pop("extras", ["all", "odd", "even"]),
            flags=kwargs.pop("flags", ["A", "B", "C", "D", "E"]),
            role=kwargs.pop("role", "style"),
            **kwargs
        )


import _plotly_utils.basevalidators


class FillValidator(_plotly_utils.basevalidators.NumberValidator):
    def __init__(self, plotly_name="fill", parent_name="isosurface.surface", **kwargs):
        super(FillValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "calc"),
            max=kwargs.pop("max", 1),
            min=kwargs.pop("min", 0),
            role=kwargs.pop("role", "style"),
            **kwargs
        )


import _plotly_utils.basevalidators


class CountValidator(_plotly_utils.basevalidators.IntegerValidator):
    def __init__(self, plotly_name="count", parent_name="isosurface.surface", **kwargs):
        super(CountValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "calc"),
            min=kwargs.pop("min", 1),
            role=kwargs.pop("role", "info"),
            **kwargs
        )
