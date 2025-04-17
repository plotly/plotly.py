import _plotly_utils.basevalidators as _bv


class StepdefaultsValidator(_bv.CompoundValidator):
    def __init__(
        self, plotly_name="stepdefaults", parent_name="indicator.gauge", **kwargs
    ):
        super().__init__(
            plotly_name,
            parent_name,
            data_class_str=kwargs.pop("data_class_str", "Step"),
            data_docs=kwargs.pop(
                "data_docs",
                """
""",
            ),
            **kwargs,
        )
