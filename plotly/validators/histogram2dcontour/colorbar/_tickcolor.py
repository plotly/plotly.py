import _plotly_utils.basevalidators as _bv


class TickcolorValidator(_bv.ColorValidator):
    def __init__(
        self,
        plotly_name="tickcolor",
        parent_name="histogram2dcontour.colorbar",
        **kwargs,
    ):
        super().__init__(
            plotly_name,
            parent_name,
            edit_type=kwargs.pop("edit_type", "colorbars"),
            **kwargs,
        )
