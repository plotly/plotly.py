import _plotly_utils.basevalidators


class TypesrcValidator(_plotly_utils.basevalidators.SrcValidator):
    def __init__(
        self,
        plotly_name="typesrc",
        parent_name="scatterternary.marker.gradient",
        **kwargs
    ):
        super(TypesrcValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "none"),
            role=kwargs.pop("role", "info"),
            **kwargs
        )


import _plotly_utils.basevalidators


class TypeValidator(_plotly_utils.basevalidators.EnumeratedValidator):
    def __init__(
        self, plotly_name="type", parent_name="scatterternary.marker.gradient", **kwargs
    ):
        super(TypeValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            array_ok=kwargs.pop("array_ok", True),
            edit_type=kwargs.pop("edit_type", "calc"),
            role=kwargs.pop("role", "style"),
            values=kwargs.pop("values", ["radial", "horizontal", "vertical", "none"]),
            **kwargs
        )


import _plotly_utils.basevalidators


class ColorsrcValidator(_plotly_utils.basevalidators.SrcValidator):
    def __init__(
        self,
        plotly_name="colorsrc",
        parent_name="scatterternary.marker.gradient",
        **kwargs
    ):
        super(ColorsrcValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "none"),
            role=kwargs.pop("role", "info"),
            **kwargs
        )


import _plotly_utils.basevalidators


class ColorValidator(_plotly_utils.basevalidators.ColorValidator):
    def __init__(
        self,
        plotly_name="color",
        parent_name="scatterternary.marker.gradient",
        **kwargs
    ):
        super(ColorValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            array_ok=kwargs.pop("array_ok", True),
            edit_type=kwargs.pop("edit_type", "calc"),
            role=kwargs.pop("role", "style"),
            **kwargs
        )
