import _plotly_utils.basevalidators


class AreaValidator(_plotly_utils.basevalidators.CompoundArrayValidator):
    def __init__(
        self, plotly_name="area", parent_name="layout.template.data", **kwargs
    ):
        super(AreaValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str=kwargs.pop("data_class_str", "Area"),
            data_docs=kwargs.pop(
                "data_docs",
                """
""",
            ),
            **kwargs
        )
