import _plotly_utils.basevalidators as _bv


class ZmidValidator(_bv.NumberValidator):
    def __init__(self, plotly_name="zmid", parent_name="heatmap", **kwargs):
        super().__init__(
            plotly_name,
            parent_name,
            edit_type=kwargs.pop("edit_type", "calc"),
            implied_edits=kwargs.pop("implied_edits", {}),
            **kwargs,
        )
