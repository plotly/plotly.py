import _plotly_utils.basevalidators as _bv


class TicklabelmodeValidator(_bv.EnumeratedValidator):
    def __init__(
        self, plotly_name="ticklabelmode", parent_name="layout.xaxis", **kwargs
    ):
        super().__init__(
            plotly_name,
            parent_name,
            edit_type=kwargs.pop("edit_type", "ticks"),
            values=kwargs.pop("values", ["instant", "period"]),
            **kwargs,
        )
