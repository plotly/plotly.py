import _plotly_utils.basevalidators as _bv


class ColumnValidator(_bv.IntegerValidator):
    def __init__(
        self, plotly_name="column", parent_name="layout.polar.domain", **kwargs
    ):
        super().__init__(
            plotly_name,
            parent_name,
            edit_type=kwargs.pop("edit_type", "plot"),
            min=kwargs.pop("min", 0),
            **kwargs,
        )
