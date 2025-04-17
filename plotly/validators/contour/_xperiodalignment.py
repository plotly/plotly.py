import _plotly_utils.basevalidators as _bv


class XperiodalignmentValidator(_bv.EnumeratedValidator):
    def __init__(self, plotly_name="xperiodalignment", parent_name="contour", **kwargs):
        super().__init__(
            plotly_name,
            parent_name,
            edit_type=kwargs.pop("edit_type", "calc"),
            implied_edits=kwargs.pop("implied_edits", {"xtype": "scaled"}),
            values=kwargs.pop("values", ["start", "middle", "end"]),
            **kwargs,
        )
