import _plotly_utils.basevalidators as _bv


class OrientationValidator(_bv.EnumeratedValidator):
    def __init__(
        self,
        plotly_name="orientation",
        parent_name="scatterternary.marker.colorbar",
        **kwargs,
    ):
        super().__init__(
            plotly_name,
            parent_name,
            edit_type=kwargs.pop("edit_type", "colorbars"),
            values=kwargs.pop("values", ["h", "v"]),
            **kwargs,
        )
