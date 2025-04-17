import _plotly_utils.basevalidators as _bv


class HovertextValidator(_bv.DataArrayValidator):
    def __init__(self, plotly_name="hovertext", parent_name="image", **kwargs):
        super().__init__(
            plotly_name,
            parent_name,
            edit_type=kwargs.pop("edit_type", "plot"),
            **kwargs,
        )
