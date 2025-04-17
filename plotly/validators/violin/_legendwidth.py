import _plotly_utils.basevalidators as _bv


class LegendwidthValidator(_bv.NumberValidator):
    def __init__(self, plotly_name="legendwidth", parent_name="violin", **kwargs):
        super().__init__(
            plotly_name,
            parent_name,
            edit_type=kwargs.pop("edit_type", "style"),
            min=kwargs.pop("min", 0),
            **kwargs,
        )
