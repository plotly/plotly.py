import _plotly_utils.basevalidators as _bv


class LatValidator(_bv.NumberValidator):
    def __init__(self, plotly_name="lat", parent_name="layout.geo.center", **kwargs):
        super().__init__(
            plotly_name,
            parent_name,
            edit_type=kwargs.pop("edit_type", "plot"),
            **kwargs,
        )
