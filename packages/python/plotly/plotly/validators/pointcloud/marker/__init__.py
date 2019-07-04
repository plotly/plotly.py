import _plotly_utils.basevalidators


class SizeminValidator(_plotly_utils.basevalidators.NumberValidator):
    def __init__(
        self, plotly_name="sizemin", parent_name="pointcloud.marker", **kwargs
    ):
        super(SizeminValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "calc"),
            max=kwargs.pop("max", 2),
            min=kwargs.pop("min", 0.1),
            role=kwargs.pop("role", "style"),
            **kwargs
        )


import _plotly_utils.basevalidators


class SizemaxValidator(_plotly_utils.basevalidators.NumberValidator):
    def __init__(
        self, plotly_name="sizemax", parent_name="pointcloud.marker", **kwargs
    ):
        super(SizemaxValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "calc"),
            min=kwargs.pop("min", 0.1),
            role=kwargs.pop("role", "style"),
            **kwargs
        )


import _plotly_utils.basevalidators


class OpacityValidator(_plotly_utils.basevalidators.NumberValidator):
    def __init__(
        self, plotly_name="opacity", parent_name="pointcloud.marker", **kwargs
    ):
        super(OpacityValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            array_ok=kwargs.pop("array_ok", False),
            edit_type=kwargs.pop("edit_type", "calc"),
            max=kwargs.pop("max", 1),
            min=kwargs.pop("min", 0),
            role=kwargs.pop("role", "style"),
            **kwargs
        )


import _plotly_utils.basevalidators


class ColorValidator(_plotly_utils.basevalidators.ColorValidator):
    def __init__(self, plotly_name="color", parent_name="pointcloud.marker", **kwargs):
        super(ColorValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            array_ok=kwargs.pop("array_ok", False),
            edit_type=kwargs.pop("edit_type", "calc"),
            role=kwargs.pop("role", "style"),
            **kwargs
        )


import _plotly_utils.basevalidators


class BorderValidator(_plotly_utils.basevalidators.CompoundValidator):
    def __init__(self, plotly_name="border", parent_name="pointcloud.marker", **kwargs):
        super(BorderValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str=kwargs.pop("data_class_str", "Border"),
            data_docs=kwargs.pop(
                "data_docs",
                """
            arearatio
                Specifies what fraction of the marker area is
                covered with the border.
            color
                Sets the stroke color. It accepts a specific
                color. If the color is not fully opaque and
                there are hundreds of thousands of points, it
                may cause slower zooming and panning.
""",
            ),
            **kwargs
        )


import _plotly_utils.basevalidators


class BlendValidator(_plotly_utils.basevalidators.BooleanValidator):
    def __init__(self, plotly_name="blend", parent_name="pointcloud.marker", **kwargs):
        super(BlendValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "calc"),
            role=kwargs.pop("role", "style"),
            **kwargs
        )
