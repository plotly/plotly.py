import _plotly_utils.basevalidators


class StepsValidator(_plotly_utils.basevalidators.CompoundValidator):
    def __init__(self, plotly_name="steps", parent_name="indicator.gauge", **kwargs):
        super(StepsValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str=kwargs.pop("data_class_str", "Steps"),
            data_docs=kwargs.pop(
                "data_docs",
                """
""",
            ),
            **kwargs
        )
