import _plotly_utils.basevalidators


class WidthValidator(_plotly_utils.basevalidators.NumberValidator):
    def __init__(self, plotly_name="width", parent_name="surface.contours.x", **kwargs):
        super(WidthValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "calc"),
            max=kwargs.pop("max", 16),
            min=kwargs.pop("min", 1),
            role=kwargs.pop("role", "style"),
            **kwargs
        )


import _plotly_utils.basevalidators


class UsecolormapValidator(_plotly_utils.basevalidators.BooleanValidator):
    def __init__(
        self, plotly_name="usecolormap", parent_name="surface.contours.x", **kwargs
    ):
        super(UsecolormapValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "calc"),
            role=kwargs.pop("role", "info"),
            **kwargs
        )


import _plotly_utils.basevalidators


class StartValidator(_plotly_utils.basevalidators.NumberValidator):
    def __init__(self, plotly_name="start", parent_name="surface.contours.x", **kwargs):
        super(StartValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "calc"),
            role=kwargs.pop("role", "style"),
            **kwargs
        )


import _plotly_utils.basevalidators


class SizeValidator(_plotly_utils.basevalidators.NumberValidator):
    def __init__(self, plotly_name="size", parent_name="surface.contours.x", **kwargs):
        super(SizeValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "calc"),
            min=kwargs.pop("min", 0),
            role=kwargs.pop("role", "style"),
            **kwargs
        )


import _plotly_utils.basevalidators


class ShowValidator(_plotly_utils.basevalidators.BooleanValidator):
    def __init__(self, plotly_name="show", parent_name="surface.contours.x", **kwargs):
        super(ShowValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "calc"),
            role=kwargs.pop("role", "info"),
            **kwargs
        )


import _plotly_utils.basevalidators


class ProjectValidator(_plotly_utils.basevalidators.CompoundValidator):
    def __init__(
        self, plotly_name="project", parent_name="surface.contours.x", **kwargs
    ):
        super(ProjectValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str=kwargs.pop("data_class_str", "Project"),
            data_docs=kwargs.pop(
                "data_docs",
                """
            x
                Determines whether or not these contour lines
                are projected on the x plane. If `highlight` is
                set to True (the default), the projected lines
                are shown on hover. If `show` is set to True,
                the projected lines are shown in permanence.
            y
                Determines whether or not these contour lines
                are projected on the y plane. If `highlight` is
                set to True (the default), the projected lines
                are shown on hover. If `show` is set to True,
                the projected lines are shown in permanence.
            z
                Determines whether or not these contour lines
                are projected on the z plane. If `highlight` is
                set to True (the default), the projected lines
                are shown on hover. If `show` is set to True,
                the projected lines are shown in permanence.
""",
            ),
            **kwargs
        )


import _plotly_utils.basevalidators


class HighlightwidthValidator(_plotly_utils.basevalidators.NumberValidator):
    def __init__(
        self, plotly_name="highlightwidth", parent_name="surface.contours.x", **kwargs
    ):
        super(HighlightwidthValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "calc"),
            max=kwargs.pop("max", 16),
            min=kwargs.pop("min", 1),
            role=kwargs.pop("role", "style"),
            **kwargs
        )


import _plotly_utils.basevalidators


class HighlightcolorValidator(_plotly_utils.basevalidators.ColorValidator):
    def __init__(
        self, plotly_name="highlightcolor", parent_name="surface.contours.x", **kwargs
    ):
        super(HighlightcolorValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "calc"),
            role=kwargs.pop("role", "style"),
            **kwargs
        )


import _plotly_utils.basevalidators


class HighlightValidator(_plotly_utils.basevalidators.BooleanValidator):
    def __init__(
        self, plotly_name="highlight", parent_name="surface.contours.x", **kwargs
    ):
        super(HighlightValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "calc"),
            role=kwargs.pop("role", "info"),
            **kwargs
        )


import _plotly_utils.basevalidators


class EndValidator(_plotly_utils.basevalidators.NumberValidator):
    def __init__(self, plotly_name="end", parent_name="surface.contours.x", **kwargs):
        super(EndValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "calc"),
            role=kwargs.pop("role", "style"),
            **kwargs
        )


import _plotly_utils.basevalidators


class ColorValidator(_plotly_utils.basevalidators.ColorValidator):
    def __init__(self, plotly_name="color", parent_name="surface.contours.x", **kwargs):
        super(ColorValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "calc"),
            role=kwargs.pop("role", "style"),
            **kwargs
        )
