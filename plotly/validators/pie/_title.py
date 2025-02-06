import _plotly_utils.basevalidators


class TitleValidator(_plotly_utils.basevalidators.TitleValidator):
    def __init__(self, plotly_name="title", parent_name="pie", **kwargs):
        super(TitleValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str=kwargs.pop("data_class_str", "Title"),
            data_docs=kwargs.pop(
                "data_docs",
                """
            font
                Sets the font used for `title`.
            position
                Specifies the location of the `title`.
            text
                Sets the title of the chart. If it is empty, no
                title is displayed.
""",
            ),
            **kwargs,
        )
