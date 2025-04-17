import _plotly_utils.basevalidators as _bv


class AutomarginValidator(_bv.BooleanValidator):
    def __init__(self, plotly_name="automargin", parent_name="pie", **kwargs):
        super().__init__(
            plotly_name,
            parent_name,
            edit_type=kwargs.pop("edit_type", "plot"),
            **kwargs,
        )
