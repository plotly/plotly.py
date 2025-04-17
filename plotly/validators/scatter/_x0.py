import _plotly_utils.basevalidators as _bv


class X0Validator(_bv.AnyValidator):
    def __init__(self, plotly_name="x0", parent_name="scatter", **kwargs):
        super().__init__(
            plotly_name,
            parent_name,
            anim=kwargs.pop("anim", True),
            edit_type=kwargs.pop("edit_type", "calc+clearAxisTypes"),
            **kwargs,
        )
