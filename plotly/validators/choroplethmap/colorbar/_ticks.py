import _plotly_utils.basevalidators as _bv


class TicksValidator(_bv.EnumeratedValidator):
    def __init__(
        self, plotly_name="ticks", parent_name="choroplethmap.colorbar", **kwargs
    ):
        super().__init__(
            plotly_name,
            parent_name,
            edit_type=kwargs.pop("edit_type", "colorbars"),
            values=kwargs.pop("values", ["outside", "inside", ""]),
            **kwargs,
        )
