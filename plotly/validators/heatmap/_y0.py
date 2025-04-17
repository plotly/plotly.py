import _plotly_utils.basevalidators as _bv


class Y0Validator(_bv.AnyValidator):
    def __init__(self, plotly_name="y0", parent_name="heatmap", **kwargs):
        super().__init__(
            plotly_name,
            parent_name,
            edit_type=kwargs.pop("edit_type", "calc+clearAxisTypes"),
            implied_edits=kwargs.pop("implied_edits", {"ytype": "scaled"}),
            **kwargs,
        )
