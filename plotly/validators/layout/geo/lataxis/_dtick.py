import _plotly_utils.basevalidators as _bv


class DtickValidator(_bv.NumberValidator):
    def __init__(self, plotly_name="dtick", parent_name="layout.geo.lataxis", **kwargs):
        super().__init__(
            plotly_name,
            parent_name,
            edit_type=kwargs.pop("edit_type", "plot"),
            **kwargs,
        )
