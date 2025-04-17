import _plotly_utils.basevalidators as _bv


class LonsrcValidator(_bv.SrcValidator):
    def __init__(self, plotly_name="lonsrc", parent_name="densitymap", **kwargs):
        super().__init__(
            plotly_name,
            parent_name,
            edit_type=kwargs.pop("edit_type", "none"),
            **kwargs,
        )
