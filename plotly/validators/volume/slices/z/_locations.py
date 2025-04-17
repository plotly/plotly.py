import _plotly_utils.basevalidators as _bv


class LocationsValidator(_bv.DataArrayValidator):
    def __init__(
        self, plotly_name="locations", parent_name="volume.slices.z", **kwargs
    ):
        super().__init__(
            plotly_name,
            parent_name,
            edit_type=kwargs.pop("edit_type", "calc"),
            **kwargs,
        )
