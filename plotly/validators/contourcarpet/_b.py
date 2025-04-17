import _plotly_utils.basevalidators as _bv


class BValidator(_bv.DataArrayValidator):
    def __init__(self, plotly_name="b", parent_name="contourcarpet", **kwargs):
        super().__init__(
            plotly_name,
            parent_name,
            edit_type=kwargs.pop("edit_type", "calc+clearAxisTypes"),
            implied_edits=kwargs.pop("implied_edits", {"ytype": "array"}),
            **kwargs,
        )
