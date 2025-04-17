import _plotly_utils.basevalidators as _bv


class ColumnordersrcValidator(_bv.SrcValidator):
    def __init__(self, plotly_name="columnordersrc", parent_name="table", **kwargs):
        super().__init__(
            plotly_name,
            parent_name,
            edit_type=kwargs.pop("edit_type", "none"),
            **kwargs,
        )
