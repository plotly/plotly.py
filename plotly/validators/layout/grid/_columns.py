import _plotly_utils.basevalidators as _bv


class ColumnsValidator(_bv.IntegerValidator):
    def __init__(self, plotly_name="columns", parent_name="layout.grid", **kwargs):
        super().__init__(
            plotly_name,
            parent_name,
            edit_type=kwargs.pop("edit_type", "plot"),
            min=kwargs.pop("min", 1),
            **kwargs,
        )
