import _plotly_utils.basevalidators


class OpacitysrcValidator(_plotly_utils.basevalidators.SrcValidator):
    def __init__(
        self, plotly_name="opacitysrc", parent_name="choroplethmapbox.marker", **kwargs
    ):
        super(OpacitysrcValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "none"),
            role=kwargs.pop("role", "info"),
            **kwargs
        )


import _plotly_utils.basevalidators


class OpacityValidator(_plotly_utils.basevalidators.NumberValidator):
    def __init__(
        self, plotly_name="opacity", parent_name="choroplethmapbox.marker", **kwargs
    ):
        super(OpacityValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            array_ok=kwargs.pop("array_ok", True),
            edit_type=kwargs.pop("edit_type", "plot"),
            max=kwargs.pop("max", 1),
            min=kwargs.pop("min", 0),
            role=kwargs.pop("role", "style"),
            **kwargs
        )


import _plotly_utils.basevalidators


class LineValidator(_plotly_utils.basevalidators.CompoundValidator):
    def __init__(
        self, plotly_name="line", parent_name="choroplethmapbox.marker", **kwargs
    ):
        super(LineValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str=kwargs.pop("data_class_str", "Line"),
            data_docs=kwargs.pop(
                "data_docs",
                """
            color
                Sets themarker.linecolor. It accepts either a
                specific color or an array of numbers that are
                mapped to the colorscale relative to the max
                and min values of the array or relative to
                `marker.line.cmin` and `marker.line.cmax` if
                set.
            colorsrc
                Sets the source reference on Chart Studio Cloud
                for  color .
            width
                Sets the width (in px) of the lines bounding
                the marker points.
            widthsrc
                Sets the source reference on Chart Studio Cloud
                for  width .
""",
            ),
            **kwargs
        )
