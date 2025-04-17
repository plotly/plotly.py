import _plotly_utils.basevalidators as _bv


class RowValidator(_bv.IntegerValidator):
    def __init__(self, plotly_name="row", parent_name="layout.smith.domain", **kwargs):
        super().__init__(
            plotly_name,
            parent_name,
            edit_type=kwargs.pop("edit_type", "plot"),
            min=kwargs.pop("min", 0),
            **kwargs,
        )
