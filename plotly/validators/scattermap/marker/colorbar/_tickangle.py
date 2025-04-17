import _plotly_utils.basevalidators as _bv


class TickangleValidator(_bv.AngleValidator):
    def __init__(
        self,
        plotly_name="tickangle",
        parent_name="scattermap.marker.colorbar",
        **kwargs,
    ):
        super().__init__(
            plotly_name,
            parent_name,
            edit_type=kwargs.pop("edit_type", "calc"),
            **kwargs,
        )
