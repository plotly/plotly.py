import _plotly_utils.basevalidators as _bv


class SourcesrcValidator(_bv.SrcValidator):
    def __init__(self, plotly_name="sourcesrc", parent_name="sankey.link", **kwargs):
        super().__init__(
            plotly_name,
            parent_name,
            edit_type=kwargs.pop("edit_type", "none"),
            **kwargs,
        )
