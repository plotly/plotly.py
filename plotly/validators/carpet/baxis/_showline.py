import _plotly_utils.basevalidators as _bv


class ShowlineValidator(_bv.BooleanValidator):
    def __init__(self, plotly_name="showline", parent_name="carpet.baxis", **kwargs):
        super().__init__(
            plotly_name,
            parent_name,
            edit_type=kwargs.pop("edit_type", "calc"),
            **kwargs,
        )
