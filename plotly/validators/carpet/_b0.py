import _plotly_utils.basevalidators as _bv


class B0Validator(_bv.NumberValidator):
    def __init__(self, plotly_name="b0", parent_name="carpet", **kwargs):
        super().__init__(
            plotly_name,
            parent_name,
            edit_type=kwargs.pop("edit_type", "calc"),
            **kwargs,
        )
