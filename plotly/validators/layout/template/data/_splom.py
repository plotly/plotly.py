import _plotly_utils.basevalidators as _bv


class SplomValidator(_bv.CompoundArrayValidator):
    def __init__(
        self, plotly_name="splom", parent_name="layout.template.data", **kwargs
    ):
        super().__init__(
            plotly_name,
            parent_name,
            data_class_str=kwargs.pop("data_class_str", "Splom"),
            data_docs=kwargs.pop(
                "data_docs",
                """
""",
            ),
            **kwargs,
        )
