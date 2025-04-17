import _plotly_utils.basevalidators as _bv


class CoordinatesValidator(_bv.AnyValidator):
    def __init__(
        self, plotly_name="coordinates", parent_name="layout.mapbox.layer", **kwargs
    ):
        super().__init__(
            plotly_name,
            parent_name,
            edit_type=kwargs.pop("edit_type", "plot"),
            **kwargs,
        )
