import _plotly_utils.basevalidators as _bv


class ZminValidator(_bv.NumberValidator):
    def __init__(self, plotly_name="zmin", parent_name="contourcarpet", **kwargs):
        super().__init__(
            plotly_name,
            parent_name,
            edit_type=kwargs.pop("edit_type", "plot"),
            implied_edits=kwargs.pop("implied_edits", {"zauto": False}),
            **kwargs,
        )
