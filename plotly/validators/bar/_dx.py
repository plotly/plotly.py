import _plotly_utils.basevalidators as _bv


class DxValidator(_bv.NumberValidator):
    def __init__(self, plotly_name="dx", parent_name="bar", **kwargs):
        super().__init__(
            plotly_name,
            parent_name,
            anim=kwargs.pop("anim", True),
            edit_type=kwargs.pop("edit_type", "calc"),
            **kwargs,
        )
