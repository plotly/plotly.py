import _plotly_utils.basevalidators as _bv


class SurfacecolorsrcValidator(_bv.SrcValidator):
    def __init__(self, plotly_name="surfacecolorsrc", parent_name="surface", **kwargs):
        super().__init__(
            plotly_name,
            parent_name,
            edit_type=kwargs.pop("edit_type", "none"),
            **kwargs,
        )
