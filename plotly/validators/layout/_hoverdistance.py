import _plotly_utils.basevalidators as _bv


class HoverdistanceValidator(_bv.IntegerValidator):
    def __init__(self, plotly_name="hoverdistance", parent_name="layout", **kwargs):
        super().__init__(
            plotly_name,
            parent_name,
            edit_type=kwargs.pop("edit_type", "none"),
            min=kwargs.pop("min", -1),
            **kwargs,
        )
