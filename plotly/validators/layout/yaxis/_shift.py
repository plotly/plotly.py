import _plotly_utils.basevalidators as _bv


class ShiftValidator(_bv.NumberValidator):
    def __init__(self, plotly_name="shift", parent_name="layout.yaxis", **kwargs):
        super().__init__(
            plotly_name,
            parent_name,
            edit_type=kwargs.pop("edit_type", "plot"),
            **kwargs,
        )
