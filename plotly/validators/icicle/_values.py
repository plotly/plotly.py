import _plotly_utils.basevalidators as _bv


class ValuesValidator(_bv.DataArrayValidator):
    def __init__(self, plotly_name="values", parent_name="icicle", **kwargs):
        super().__init__(
            plotly_name,
            parent_name,
            edit_type=kwargs.pop("edit_type", "calc"),
            **kwargs,
        )
