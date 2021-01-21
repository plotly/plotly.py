import _plotly_utils.basevalidators


class ShapesValidator(_plotly_utils.basevalidators.CompoundValidator):
    def __init__(self, plotly_name="shapes", parent_name="layout", **kwargs):
        super(ShapesValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str=kwargs.pop("data_class_str", "Shapes"),
            data_docs=kwargs.pop(
                "data_docs",
                """
""",
            ),
            **kwargs
        )
