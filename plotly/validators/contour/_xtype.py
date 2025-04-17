import _plotly_utils.basevalidators as _bv


class XtypeValidator(_bv.EnumeratedValidator):
    def __init__(self, plotly_name="xtype", parent_name="contour", **kwargs):
        super().__init__(
            plotly_name,
            parent_name,
            edit_type=kwargs.pop("edit_type", "calc+clearAxisTypes"),
            values=kwargs.pop("values", ["array", "scaled"]),
            **kwargs,
        )
