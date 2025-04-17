import _plotly_utils.basevalidators as _bv


class ShowspikesValidator(_bv.BooleanValidator):
    def __init__(self, plotly_name="showspikes", parent_name="layout.yaxis", **kwargs):
        super().__init__(
            plotly_name,
            parent_name,
            edit_type=kwargs.pop("edit_type", "modebar"),
            **kwargs,
        )
