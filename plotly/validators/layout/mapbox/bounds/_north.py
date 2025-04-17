import _plotly_utils.basevalidators as _bv


class NorthValidator(_bv.NumberValidator):
    def __init__(
        self, plotly_name="north", parent_name="layout.mapbox.bounds", **kwargs
    ):
        super().__init__(
            plotly_name,
            parent_name,
            edit_type=kwargs.pop("edit_type", "plot"),
            **kwargs,
        )
