import _plotly_utils.basevalidators as _bv


class MetasrcValidator(_bv.SrcValidator):
    def __init__(self, plotly_name="metasrc", parent_name="scatterpolar", **kwargs):
        super().__init__(
            plotly_name,
            parent_name,
            edit_type=kwargs.pop("edit_type", "none"),
            **kwargs,
        )
