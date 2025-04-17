import _plotly_utils.basevalidators as _bv


class ShowsubunitsValidator(_bv.BooleanValidator):
    def __init__(self, plotly_name="showsubunits", parent_name="layout.geo", **kwargs):
        super().__init__(
            plotly_name,
            parent_name,
            edit_type=kwargs.pop("edit_type", "plot"),
            **kwargs,
        )
