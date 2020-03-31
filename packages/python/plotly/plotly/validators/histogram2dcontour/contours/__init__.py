import _plotly_utils.basevalidators


class ValueValidator(_plotly_utils.basevalidators.AnyValidator):
    def __init__(
        self, plotly_name="value", parent_name="histogram2dcontour.contours", **kwargs
    ):
        super(ValueValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "calc"),
            role=kwargs.pop("role", "info"),
            **kwargs
        )


import _plotly_utils.basevalidators


class TypeValidator(_plotly_utils.basevalidators.EnumeratedValidator):
    def __init__(
        self, plotly_name="type", parent_name="histogram2dcontour.contours", **kwargs
    ):
        super(TypeValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "calc"),
            role=kwargs.pop("role", "info"),
            values=kwargs.pop("values", ["levels", "constraint"]),
            **kwargs
        )


import _plotly_utils.basevalidators


class StartValidator(_plotly_utils.basevalidators.NumberValidator):
    def __init__(
        self, plotly_name="start", parent_name="histogram2dcontour.contours", **kwargs
    ):
        super(StartValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "plot"),
            implied_edits=kwargs.pop("implied_edits", {"^autocontour": False}),
            role=kwargs.pop("role", "style"),
            **kwargs
        )


import _plotly_utils.basevalidators


class SizeValidator(_plotly_utils.basevalidators.NumberValidator):
    def __init__(
        self, plotly_name="size", parent_name="histogram2dcontour.contours", **kwargs
    ):
        super(SizeValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "plot"),
            implied_edits=kwargs.pop("implied_edits", {"^autocontour": False}),
            min=kwargs.pop("min", 0),
            role=kwargs.pop("role", "style"),
            **kwargs
        )


import _plotly_utils.basevalidators


class ShowlinesValidator(_plotly_utils.basevalidators.BooleanValidator):
    def __init__(
        self,
        plotly_name="showlines",
        parent_name="histogram2dcontour.contours",
        **kwargs
    ):
        super(ShowlinesValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "plot"),
            role=kwargs.pop("role", "style"),
            **kwargs
        )


import _plotly_utils.basevalidators


class ShowlabelsValidator(_plotly_utils.basevalidators.BooleanValidator):
    def __init__(
        self,
        plotly_name="showlabels",
        parent_name="histogram2dcontour.contours",
        **kwargs
    ):
        super(ShowlabelsValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "plot"),
            role=kwargs.pop("role", "style"),
            **kwargs
        )


import _plotly_utils.basevalidators


class OperationValidator(_plotly_utils.basevalidators.EnumeratedValidator):
    def __init__(
        self,
        plotly_name="operation",
        parent_name="histogram2dcontour.contours",
        **kwargs
    ):
        super(OperationValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "calc"),
            role=kwargs.pop("role", "info"),
            values=kwargs.pop(
                "values",
                [
                    "=",
                    "<",
                    ">=",
                    ">",
                    "<=",
                    "[]",
                    "()",
                    "[)",
                    "(]",
                    "][",
                    ")(",
                    "](",
                    ")[",
                ],
            ),
            **kwargs
        )


import _plotly_utils.basevalidators


class LabelformatValidator(_plotly_utils.basevalidators.StringValidator):
    def __init__(
        self,
        plotly_name="labelformat",
        parent_name="histogram2dcontour.contours",
        **kwargs
    ):
        super(LabelformatValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "plot"),
            role=kwargs.pop("role", "style"),
            **kwargs
        )


import _plotly_utils.basevalidators


class LabelfontValidator(_plotly_utils.basevalidators.CompoundValidator):
    def __init__(
        self,
        plotly_name="labelfont",
        parent_name="histogram2dcontour.contours",
        **kwargs
    ):
        super(LabelfontValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str=kwargs.pop("data_class_str", "Labelfont"),
            data_docs=kwargs.pop(
                "data_docs",
                """
            color

            family
                HTML font family - the typeface that will be
                applied by the web browser. The web browser
                will only be able to apply a font if it is
                available on the system which it operates.
                Provide multiple font families, separated by
                commas, to indicate the preference in which to
                apply fonts if they aren't available on the
                system. The Chart Studio Cloud (at
                https://chart-studio.plotly.com or on-premise)
                generates images on a server, where only a
                select number of fonts are installed and
                supported. These include "Arial", "Balto",
                "Courier New", "Droid Sans",, "Droid Serif",
                "Droid Sans Mono", "Gravitas One", "Old
                Standard TT", "Open Sans", "Overpass", "PT Sans
                Narrow", "Raleway", "Times New Roman".
            size

""",
            ),
            **kwargs
        )


import _plotly_utils.basevalidators


class EndValidator(_plotly_utils.basevalidators.NumberValidator):
    def __init__(
        self, plotly_name="end", parent_name="histogram2dcontour.contours", **kwargs
    ):
        super(EndValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "plot"),
            implied_edits=kwargs.pop("implied_edits", {"^autocontour": False}),
            role=kwargs.pop("role", "style"),
            **kwargs
        )


import _plotly_utils.basevalidators


class ColoringValidator(_plotly_utils.basevalidators.EnumeratedValidator):
    def __init__(
        self,
        plotly_name="coloring",
        parent_name="histogram2dcontour.contours",
        **kwargs
    ):
        super(ColoringValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "calc"),
            role=kwargs.pop("role", "style"),
            values=kwargs.pop("values", ["fill", "heatmap", "lines", "none"]),
            **kwargs
        )
