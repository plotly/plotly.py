import _plotly_utils.basevalidators as _bv


class TickformatstopdefaultsValidator(_bv.CompoundValidator):
    def __init__(
        self,
        plotly_name="tickformatstopdefaults",
        parent_name="layout.ternary.caxis",
        **kwargs,
    ):
        super().__init__(
            plotly_name,
            parent_name,
            data_class_str=kwargs.pop("data_class_str", "Tickformatstop"),
            data_docs=kwargs.pop(
                "data_docs",
                """
""",
            ),
            **kwargs,
        )
