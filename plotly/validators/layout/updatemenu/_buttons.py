import _plotly_utils.basevalidators as _bv


class ButtonsValidator(_bv.CompoundArrayValidator):
    def __init__(
        self, plotly_name="buttons", parent_name="layout.updatemenu", **kwargs
    ):
        super().__init__(
            plotly_name,
            parent_name,
            data_class_str=kwargs.pop("data_class_str", "Button"),
            data_docs=kwargs.pop(
                "data_docs",
                """
""",
            ),
            **kwargs,
        )
