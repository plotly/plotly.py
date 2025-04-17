import _plotly_utils.basevalidators as _bv


class ShowValidator(_bv.BooleanValidator):
    def __init__(self, plotly_name="show", parent_name="mesh3d.contour", **kwargs):
        super().__init__(
            plotly_name,
            parent_name,
            edit_type=kwargs.pop("edit_type", "calc"),
            **kwargs,
        )
