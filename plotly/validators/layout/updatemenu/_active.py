import _plotly_utils.basevalidators as _bv


class ActiveValidator(_bv.IntegerValidator):
    def __init__(self, plotly_name="active", parent_name="layout.updatemenu", **kwargs):
        super().__init__(
            plotly_name,
            parent_name,
            edit_type=kwargs.pop("edit_type", "arraydraw"),
            min=kwargs.pop("min", -1),
            **kwargs,
        )
