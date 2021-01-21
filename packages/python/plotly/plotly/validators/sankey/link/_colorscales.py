import _plotly_utils.basevalidators


class ColorscalesValidator(_plotly_utils.basevalidators.CompoundValidator):
    def __init__(self, plotly_name="colorscales", parent_name="sankey.link", **kwargs):
        super(ColorscalesValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str=kwargs.pop("data_class_str", "Colorscales"),
            data_docs=kwargs.pop(
                "data_docs",
                """
""",
            ),
            **kwargs
        )
