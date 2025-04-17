import _plotly_utils.basevalidators as _bv


class ButtondefaultsValidator(_bv.CompoundValidator):
    def __init__(
        self,
        plotly_name="buttondefaults",
        parent_name="layout.xaxis.rangeselector",
        **kwargs,
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
