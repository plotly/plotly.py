import _plotly_utils.basevalidators as _bv


class LinepositionValidator(_bv.FlaglistValidator):
    def __init__(
        self,
        plotly_name="lineposition",
        parent_name="indicator.gauge.axis.tickfont",
        **kwargs,
    ):
        super().__init__(
            plotly_name,
            parent_name,
            edit_type=kwargs.pop("edit_type", "plot"),
            extras=kwargs.pop("extras", ["none"]),
            flags=kwargs.pop("flags", ["under", "over", "through"]),
            **kwargs,
        )
