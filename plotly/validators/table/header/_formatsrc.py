import _plotly_utils.basevalidators as _bv


class FormatsrcValidator(_bv.SrcValidator):
    def __init__(self, plotly_name="formatsrc", parent_name="table.header", **kwargs):
        super().__init__(
            plotly_name,
            parent_name,
            edit_type=kwargs.pop("edit_type", "none"),
            **kwargs,
        )
