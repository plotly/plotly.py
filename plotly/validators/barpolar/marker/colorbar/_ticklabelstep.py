import _plotly_utils.basevalidators as _bv


class TicklabelstepValidator(_bv.IntegerValidator):
    def __init__(
        self,
        plotly_name="ticklabelstep",
        parent_name="barpolar.marker.colorbar",
        **kwargs,
    ):
        super().__init__(
            plotly_name,
            parent_name,
            edit_type=kwargs.pop("edit_type", "colorbars"),
            min=kwargs.pop("min", 1),
            **kwargs,
        )
