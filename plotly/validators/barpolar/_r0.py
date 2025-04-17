import _plotly_utils.basevalidators as _bv


class R0Validator(_bv.AnyValidator):
    def __init__(self, plotly_name="r0", parent_name="barpolar", **kwargs):
        super().__init__(
            plotly_name,
            parent_name,
            edit_type=kwargs.pop("edit_type", "calc+clearAxisTypes"),
            **kwargs,
        )
