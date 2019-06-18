import _plotly_utils.basevalidators


class LineValidator(_plotly_utils.basevalidators.CompoundValidator):
    def __init__(self, plotly_name="line", parent_name="sunburst.marker", **kwargs):
        super(LineValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str=kwargs.pop("data_class_str", "Line"),
            data_docs=kwargs.pop(
                "data_docs",
                """
            color
                Sets the color of the line enclosing each
                sector. Defaults to the `paper_bgcolor` value.
            colorsrc
                Sets the source reference on plot.ly for  color
                .
            width
                Sets the width (in px) of the line enclosing
                each sector.
            widthsrc
                Sets the source reference on plot.ly for  width
                .
""",
            ),
            **kwargs
        )


import _plotly_utils.basevalidators


class ColorssrcValidator(_plotly_utils.basevalidators.SrcValidator):
    def __init__(
        self, plotly_name="colorssrc", parent_name="sunburst.marker", **kwargs
    ):
        super(ColorssrcValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "none"),
            role=kwargs.pop("role", "info"),
            **kwargs
        )


import _plotly_utils.basevalidators


class ColorsValidator(_plotly_utils.basevalidators.DataArrayValidator):
    def __init__(self, plotly_name="colors", parent_name="sunburst.marker", **kwargs):
        super(ColorsValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "calc"),
            role=kwargs.pop("role", "data"),
            **kwargs
        )
