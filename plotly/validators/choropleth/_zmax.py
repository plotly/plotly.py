import _plotly_utils.basevalidators as _bv


class ZmaxValidator(_bv.NumberValidator):
    def __init__(self, plotly_name="zmax", parent_name="choropleth", **kwargs):
        super().__init__(
            plotly_name,
            parent_name,
            edit_type=kwargs.pop("edit_type", "calc"),
            implied_edits=kwargs.pop("implied_edits", {"zauto": False}),
            **kwargs,
        )
