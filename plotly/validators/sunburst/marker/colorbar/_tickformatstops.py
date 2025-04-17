import _plotly_utils.basevalidators as _bv


class TickformatstopsValidator(_bv.CompoundArrayValidator):
    def __init__(
        self,
        plotly_name="tickformatstops",
        parent_name="sunburst.marker.colorbar",
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
