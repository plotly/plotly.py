import _plotly_utils.basevalidators as _bv


class RemovesrcValidator(_bv.SrcValidator):
    def __init__(self, plotly_name="removesrc", parent_name="layout.modebar", **kwargs):
        super().__init__(
            plotly_name,
            parent_name,
            edit_type=kwargs.pop("edit_type", "none"),
            **kwargs,
        )
