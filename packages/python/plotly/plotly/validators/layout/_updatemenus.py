import _plotly_utils.basevalidators


class UpdatemenusValidator(_plotly_utils.basevalidators.CompoundValidator):
    def __init__(self, plotly_name="updatemenus", parent_name="layout", **kwargs):
        super(UpdatemenusValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str=kwargs.pop("data_class_str", "Updatemenus"),
            data_docs=kwargs.pop(
                "data_docs",
                """
""",
            ),
            **kwargs
        )
