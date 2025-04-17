import _plotly_utils.basevalidators as _bv


class RangebreakdefaultsValidator(_bv.CompoundValidator):
    def __init__(
        self, plotly_name="rangebreakdefaults", parent_name="layout.yaxis", **kwargs
    ):
        super().__init__(
            plotly_name,
            parent_name,
            data_class_str=kwargs.pop("data_class_str", "Rangebreak"),
            data_docs=kwargs.pop(
                "data_docs",
                """
""",
            ),
            **kwargs,
        )
