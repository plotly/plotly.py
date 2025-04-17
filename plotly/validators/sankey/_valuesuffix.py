import _plotly_utils.basevalidators as _bv


class ValuesuffixValidator(_bv.StringValidator):
    def __init__(self, plotly_name="valuesuffix", parent_name="sankey", **kwargs):
        super().__init__(
            plotly_name,
            parent_name,
            edit_type=kwargs.pop("edit_type", "calc"),
            **kwargs,
        )
