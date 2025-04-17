import _plotly_utils.basevalidators as _bv


class ShadowsrcValidator(_bv.SrcValidator):
    def __init__(
        self, plotly_name="shadowsrc", parent_name="treemap.textfont", **kwargs
    ):
        super().__init__(
            plotly_name,
            parent_name,
            edit_type=kwargs.pop("edit_type", "none"),
            **kwargs,
        )
