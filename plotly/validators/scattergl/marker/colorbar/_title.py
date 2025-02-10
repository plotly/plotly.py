import _plotly_utils.basevalidators


class TitleValidator(_plotly_utils.basevalidators.TitleValidator):
    def __init__(
        self, plotly_name="title", parent_name="scattergl.marker.colorbar", **kwargs
    ):
        super(TitleValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str=kwargs.pop("data_class_str", "Title"),
            data_docs=kwargs.pop(
                "data_docs",
                """
            font
                Sets this color bar's title font.
            side
                Determines the location of color bar's title
                with respect to the color bar. Defaults to
                "top" when `orientation` if "v" and  defaults
                to "right" when `orientation` if "h".
            text
                Sets the title of the color bar.
""",
            ),
            **kwargs,
        )
