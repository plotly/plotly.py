import _plotly_utils.basevalidators as _bv


class NotchedValidator(_bv.BooleanValidator):
    def __init__(self, plotly_name="notched", parent_name="box", **kwargs):
        super().__init__(
            plotly_name,
            parent_name,
            edit_type=kwargs.pop("edit_type", "calc"),
            **kwargs,
        )
