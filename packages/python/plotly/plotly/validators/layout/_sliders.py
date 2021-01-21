import _plotly_utils.basevalidators


class SlidersValidator(_plotly_utils.basevalidators.CompoundValidator):
    def __init__(self, plotly_name="sliders", parent_name="layout", **kwargs):
        super(SlidersValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str=kwargs.pop("data_class_str", "Sliders"),
            data_docs=kwargs.pop(
                "data_docs",
                """
""",
            ),
            **kwargs
        )
