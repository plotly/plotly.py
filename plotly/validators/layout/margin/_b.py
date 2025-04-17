import _plotly_utils.basevalidators as _bv


class BValidator(_bv.NumberValidator):
    def __init__(self, plotly_name="b", parent_name="layout.margin", **kwargs):
        super().__init__(
            plotly_name,
            parent_name,
            edit_type=kwargs.pop("edit_type", "plot"),
            min=kwargs.pop("min", 0),
            **kwargs,
        )
