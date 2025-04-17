import _plotly_utils.basevalidators as _bv


class Label0Validator(_bv.NumberValidator):
    def __init__(self, plotly_name="label0", parent_name="pie", **kwargs):
        super().__init__(
            plotly_name,
            parent_name,
            edit_type=kwargs.pop("edit_type", "calc"),
            **kwargs,
        )
