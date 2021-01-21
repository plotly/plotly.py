import _plotly_utils.basevalidators


class RangebreaksValidator(_plotly_utils.basevalidators.CompoundValidator):
    def __init__(self, plotly_name="rangebreaks", parent_name="layout.yaxis", **kwargs):
        super(RangebreaksValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str=kwargs.pop("data_class_str", "Rangebreaks"),
            data_docs=kwargs.pop(
                "data_docs",
                """
""",
            ),
            **kwargs
        )
