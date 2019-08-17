import _plotly_utils.basevalidators


class SizeValidator(_plotly_utils.basevalidators.NumberValidator):
    def __init__(self, plotly_name="size", parent_name="box.selected.marker", **kwargs):
        super(SizeValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "style"),
            min=kwargs.pop("min", 0),
            role=kwargs.pop("role", "style"),
            **kwargs
        )


import _plotly_utils.basevalidators


class OpacityValidator(_plotly_utils.basevalidators.NumberValidator):
    def __init__(
        self, plotly_name="opacity", parent_name="box.selected.marker", **kwargs
    ):
        super(OpacityValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "style"),
            max=kwargs.pop("max", 1),
            min=kwargs.pop("min", 0),
            role=kwargs.pop("role", "style"),
            **kwargs
        )


import _plotly_utils.basevalidators


class ColorValidator(_plotly_utils.basevalidators.ColorValidator):
    def __init__(
        self, plotly_name="color", parent_name="box.selected.marker", **kwargs
    ):
        super(ColorValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "style"),
            role=kwargs.pop("role", "style"),
            **kwargs
        )
