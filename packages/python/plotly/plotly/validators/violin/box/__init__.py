import _plotly_utils.basevalidators


class WidthValidator(_plotly_utils.basevalidators.NumberValidator):
    def __init__(self, plotly_name="width", parent_name="violin.box", **kwargs):
        super(WidthValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "plot"),
            max=kwargs.pop("max", 1),
            min=kwargs.pop("min", 0),
            role=kwargs.pop("role", "info"),
            **kwargs
        )


import _plotly_utils.basevalidators


class VisibleValidator(_plotly_utils.basevalidators.BooleanValidator):
    def __init__(self, plotly_name="visible", parent_name="violin.box", **kwargs):
        super(VisibleValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "plot"),
            role=kwargs.pop("role", "info"),
            **kwargs
        )


import _plotly_utils.basevalidators


class LineValidator(_plotly_utils.basevalidators.CompoundValidator):
    def __init__(self, plotly_name="line", parent_name="violin.box", **kwargs):
        super(LineValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str=kwargs.pop("data_class_str", "Line"),
            data_docs=kwargs.pop(
                "data_docs",
                """
            color
                Sets the inner box plot bounding line color.
            width
                Sets the inner box plot bounding line width.
""",
            ),
            **kwargs
        )


import _plotly_utils.basevalidators


class FillcolorValidator(_plotly_utils.basevalidators.ColorValidator):
    def __init__(self, plotly_name="fillcolor", parent_name="violin.box", **kwargs):
        super(FillcolorValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "style"),
            role=kwargs.pop("role", "style"),
            **kwargs
        )
