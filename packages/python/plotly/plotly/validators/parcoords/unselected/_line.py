import _plotly_utils.basevalidators


class LineValidator(_plotly_utils.basevalidators.CompoundValidator):
    def __init__(
        self, plotly_name="line", parent_name="parcoords.unselected", **kwargs
    ):
        super(LineValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str=kwargs.pop("data_class_str", "Line"),
            data_docs=kwargs.pop(
                "data_docs",
                """
            color
                Sets the line color. It accepts either a
                specific color or an array of numbers that are
                mapped to the colorscale relative to the max
                and min values of the array or relative to
                `line.cmin` and `line.cmax` if set.
            opacity
                Sets the line opacity. It is a number between 0 and 1.
                0 is transparent. 1 is opaque.
""",
            ),
            **kwargs,
        )
