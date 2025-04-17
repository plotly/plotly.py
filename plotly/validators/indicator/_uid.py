import _plotly_utils.basevalidators as _bv


class UidValidator(_bv.StringValidator):
    def __init__(self, plotly_name="uid", parent_name="indicator", **kwargs):
        super().__init__(
            plotly_name,
            parent_name,
            anim=kwargs.pop("anim", True),
            edit_type=kwargs.pop("edit_type", "plot"),
            **kwargs,
        )
