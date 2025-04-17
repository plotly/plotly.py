import _plotly_utils.basevalidators as _bv


class MaxallowedValidator(_bv.AnyValidator):
    def __init__(self, plotly_name="maxallowed", parent_name="layout.yaxis", **kwargs):
        super().__init__(
            plotly_name,
            parent_name,
            edit_type=kwargs.pop("edit_type", "plot"),
            implied_edits=kwargs.pop("implied_edits", {"^autorange": False}),
            **kwargs,
        )
