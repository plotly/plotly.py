import _plotly_utils.basevalidators as _bv


class AutorangeValidator(_bv.EnumeratedValidator):
    def __init__(self, plotly_name="autorange", parent_name="carpet.aaxis", **kwargs):
        super().__init__(
            plotly_name,
            parent_name,
            edit_type=kwargs.pop("edit_type", "calc"),
            values=kwargs.pop("values", [True, False, "reversed"]),
            **kwargs,
        )
