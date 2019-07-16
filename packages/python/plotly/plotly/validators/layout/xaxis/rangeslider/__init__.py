import _plotly_utils.basevalidators


class YAxisValidator(_plotly_utils.basevalidators.CompoundValidator):
    def __init__(
        self, plotly_name="yaxis", parent_name="layout.xaxis.rangeslider", **kwargs
    ):
        super(YAxisValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str=kwargs.pop("data_class_str", "YAxis"),
            data_docs=kwargs.pop(
                "data_docs",
                """
            range
                Sets the range of this axis for the
                rangeslider.
            rangemode
                Determines whether or not the range of this
                axis in the rangeslider use the same value than
                in the main plot when zooming in/out. If
                "auto", the autorange will be used. If "fixed",
                the `range` is used. If "match", the current
                range of the corresponding y-axis on the main
                subplot is used.
""",
            ),
            **kwargs
        )


import _plotly_utils.basevalidators


class VisibleValidator(_plotly_utils.basevalidators.BooleanValidator):
    def __init__(
        self, plotly_name="visible", parent_name="layout.xaxis.rangeslider", **kwargs
    ):
        super(VisibleValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "calc"),
            role=kwargs.pop("role", "info"),
            **kwargs
        )


import _plotly_utils.basevalidators


class ThicknessValidator(_plotly_utils.basevalidators.NumberValidator):
    def __init__(
        self, plotly_name="thickness", parent_name="layout.xaxis.rangeslider", **kwargs
    ):
        super(ThicknessValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "plot"),
            max=kwargs.pop("max", 1),
            min=kwargs.pop("min", 0),
            role=kwargs.pop("role", "style"),
            **kwargs
        )


import _plotly_utils.basevalidators


class RangeValidator(_plotly_utils.basevalidators.InfoArrayValidator):
    def __init__(
        self, plotly_name="range", parent_name="layout.xaxis.rangeslider", **kwargs
    ):
        super(RangeValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "calc"),
            implied_edits=kwargs.pop("implied_edits", {"autorange": False}),
            items=kwargs.pop(
                "items",
                [
                    {
                        "valType": "any",
                        "editType": "calc",
                        "impliedEdits": {"^autorange": False},
                    },
                    {
                        "valType": "any",
                        "editType": "calc",
                        "impliedEdits": {"^autorange": False},
                    },
                ],
            ),
            role=kwargs.pop("role", "info"),
            **kwargs
        )


import _plotly_utils.basevalidators


class BorderwidthValidator(_plotly_utils.basevalidators.IntegerValidator):
    def __init__(
        self,
        plotly_name="borderwidth",
        parent_name="layout.xaxis.rangeslider",
        **kwargs
    ):
        super(BorderwidthValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "plot"),
            min=kwargs.pop("min", 0),
            role=kwargs.pop("role", "style"),
            **kwargs
        )


import _plotly_utils.basevalidators


class BordercolorValidator(_plotly_utils.basevalidators.ColorValidator):
    def __init__(
        self,
        plotly_name="bordercolor",
        parent_name="layout.xaxis.rangeslider",
        **kwargs
    ):
        super(BordercolorValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "plot"),
            role=kwargs.pop("role", "style"),
            **kwargs
        )


import _plotly_utils.basevalidators


class BgcolorValidator(_plotly_utils.basevalidators.ColorValidator):
    def __init__(
        self, plotly_name="bgcolor", parent_name="layout.xaxis.rangeslider", **kwargs
    ):
        super(BgcolorValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "plot"),
            role=kwargs.pop("role", "style"),
            **kwargs
        )


import _plotly_utils.basevalidators


class AutorangeValidator(_plotly_utils.basevalidators.BooleanValidator):
    def __init__(
        self, plotly_name="autorange", parent_name="layout.xaxis.rangeslider", **kwargs
    ):
        super(AutorangeValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "calc"),
            implied_edits=kwargs.pop("implied_edits", {}),
            role=kwargs.pop("role", "style"),
            **kwargs
        )
