import _plotly_utils.basevalidators


class ShowValidator(_plotly_utils.basevalidators.BooleanValidator):
    def __init__(self, plotly_name="show", parent_name="isosurface.caps.z", **kwargs):
        super(ShowValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "calc"),
            role=kwargs.pop("role", "info"),
            **kwargs
        )


import _plotly_utils.basevalidators


class FillValidator(_plotly_utils.basevalidators.NumberValidator):
    def __init__(self, plotly_name="fill", parent_name="isosurface.caps.z", **kwargs):
        super(FillValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "calc"),
            max=kwargs.pop("max", 1),
            min=kwargs.pop("min", 0),
            role=kwargs.pop("role", "style"),
            **kwargs
        )
