import _plotly_utils.basevalidators as _bv


class RangemodeValidator(_bv.EnumeratedValidator):
    def __init__(self, plotly_name="rangemode", parent_name="layout.yaxis", **kwargs):
        super().__init__(
            plotly_name,
            parent_name,
            edit_type=kwargs.pop("edit_type", "plot"),
            values=kwargs.pop("values", ["normal", "tozero", "nonnegative"]),
            **kwargs,
        )
