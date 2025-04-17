import _plotly_utils.basevalidators as _bv


class OffsetsrcValidator(_bv.SrcValidator):
    def __init__(self, plotly_name="offsetsrc", parent_name="waterfall", **kwargs):
        super().__init__(
            plotly_name,
            parent_name,
            edit_type=kwargs.pop("edit_type", "none"),
            **kwargs,
        )
