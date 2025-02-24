import _plotly_utils.basevalidators as _bv


class SizesrcValidator(_bv.SrcValidator):
    def __init__(
        self, plotly_name="sizesrc", parent_name="funnelarea.insidetextfont", **kwargs
    ):
        super().__init__(
            plotly_name,
            parent_name,
            edit_type=kwargs.pop("edit_type", "none"),
            **kwargs,
        )
