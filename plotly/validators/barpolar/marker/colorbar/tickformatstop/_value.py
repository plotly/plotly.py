import _plotly_utils.basevalidators as _bv


class ValueValidator(_bv.StringValidator):
    def __init__(
        self,
        plotly_name="value",
        parent_name="barpolar.marker.colorbar.tickformatstop",
        **kwargs,
    ):
        super().__init__(
            plotly_name,
            parent_name,
            edit_type=kwargs.pop("edit_type", "colorbars"),
            **kwargs,
        )
