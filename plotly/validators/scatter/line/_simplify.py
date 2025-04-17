import _plotly_utils.basevalidators as _bv


class SimplifyValidator(_bv.BooleanValidator):
    def __init__(self, plotly_name="simplify", parent_name="scatter.line", **kwargs):
        super().__init__(
            plotly_name,
            parent_name,
            edit_type=kwargs.pop("edit_type", "plot"),
            **kwargs,
        )
