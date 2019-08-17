import _plotly_utils.basevalidators


class LineValidator(_plotly_utils.basevalidators.CompoundValidator):
    def __init__(
        self, plotly_name="line", parent_name="candlestick.decreasing", **kwargs
    ):
        super(LineValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str=kwargs.pop("data_class_str", "Line"),
            data_docs=kwargs.pop(
                "data_docs",
                """
            color
                Sets the color of line bounding the box(es).
            width
                Sets the width (in px) of line bounding the
                box(es).
""",
            ),
            **kwargs
        )


import _plotly_utils.basevalidators


class FillcolorValidator(_plotly_utils.basevalidators.ColorValidator):
    def __init__(
        self, plotly_name="fillcolor", parent_name="candlestick.decreasing", **kwargs
    ):
        super(FillcolorValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "style"),
            role=kwargs.pop("role", "style"),
            **kwargs
        )
