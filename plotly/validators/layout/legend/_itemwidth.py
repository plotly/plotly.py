import _plotly_utils.basevalidators as _bv


class ItemwidthValidator(_bv.NumberValidator):
    def __init__(self, plotly_name="itemwidth", parent_name="layout.legend", **kwargs):
        super().__init__(
            plotly_name,
            parent_name,
            edit_type=kwargs.pop("edit_type", "legend"),
            min=kwargs.pop("min", 30),
            **kwargs,
        )
