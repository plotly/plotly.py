import _plotly_utils.basevalidators


class DimensionsValidator(_plotly_utils.basevalidators.CompoundValidator):
    def __init__(self, plotly_name="dimensions", parent_name="parcats", **kwargs):
        super(DimensionsValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str=kwargs.pop("data_class_str", "Dimensions"),
            data_docs=kwargs.pop(
                "data_docs",
                """
""",
            ),
            **kwargs
        )
