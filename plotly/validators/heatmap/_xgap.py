import _plotly_utils.basevalidators as _bv


class XgapValidator(_bv.NumberValidator):
    def __init__(self, plotly_name="xgap", parent_name="heatmap", **kwargs):
        super().__init__(
            plotly_name,
            parent_name,
            edit_type=kwargs.pop("edit_type", "plot"),
            min=kwargs.pop("min", 0),
            **kwargs,
        )
