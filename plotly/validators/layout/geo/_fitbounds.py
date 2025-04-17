import _plotly_utils.basevalidators as _bv


class FitboundsValidator(_bv.EnumeratedValidator):
    def __init__(self, plotly_name="fitbounds", parent_name="layout.geo", **kwargs):
        super().__init__(
            plotly_name,
            parent_name,
            edit_type=kwargs.pop("edit_type", "plot"),
            values=kwargs.pop("values", [False, "locations", "geojson"]),
            **kwargs,
        )
