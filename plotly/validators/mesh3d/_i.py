import _plotly_utils.basevalidators as _bv


class IValidator(_bv.DataArrayValidator):
    def __init__(self, plotly_name="i", parent_name="mesh3d", **kwargs):
        super().__init__(
            plotly_name,
            parent_name,
            edit_type=kwargs.pop("edit_type", "calc"),
            **kwargs,
        )
